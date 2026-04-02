import spacy
import pandas as pd
from textstat import textstat
from germansentiment import SentimentModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pyphen
from nltk.corpus import stopwords

# Mapping for stopword languages
lang_map = {"en": "english", "de": "german"}

# Files for abstractness data.
abstractness_files = {
    "de": "data/abstractness/ratings_lrec16_koeper_ssiw.txt",
    "en": "data/abstractness/13428_2013_403_MOESM1_ESM.xlsx",
}

# Pre-loaded sentiment models.
sentiment_models = {
    "de": SentimentModel(),  # Pre-loaded German sentiment model
    "en": SentimentIntensityAnalyzer()
    # Add other language-specific models if available.
}

# Spacy models per language.
spacy_models = {
    "de": "de_core_news_md",
    "en": "en_core_web_md"  # Example for English.
}

# Cache for Pyphen instances.
_PYHEN_CACHE = {}


def get_pyphen(language):
    if language not in _PYHEN_CACHE:
        _PYHEN_CACHE[language] = pyphen.Pyphen(lang=language)
    return _PYHEN_CACHE[language]


def load_resources(language):
    # Load the spacy model.
    if language not in spacy_models:
        raise ValueError(f"Language '{language}' not supported for spacy.")
    nlp = spacy.load(spacy_models[language])

    # Load and pre-process abstractness data if available.
    abstractness_lookup = None
    if language in abstractness_files:
        if language == "en":
            abs_data = pd.read_excel(abstractness_files[language])
        elif language == "de":
            abs_data = pd.read_csv(abstractness_files[language], sep='\t')
            abs_data = abs_data.drop_duplicates(subset=['Word'], keep='first')
            abs_data = abs_data.dropna(subset=['Word'])
            abs_data = abs_data.set_index('Word')  # Ensure 'Word' is the index

        # Ensure words are lower-cased and create a lookup dictionary.
        if 'Word' in abs_data.columns:
            abs_data['Word'] = abs_data['Word'].str.lower()
            # Create a lookup: word -> dict of features.
            abstractness_lookup = abs_data.set_index('Word').to_dict(orient='index')

    # Select sentiment model.
    sentiment_model = sentiment_models.get(language, None)

    stop_words_lang = set(stopwords.words(lang_map[language]))

    return nlp, abstractness_lookup, sentiment_model, stop_words_lang


def count_syllables(text, language):
    words = text.split()
    dic = get_pyphen(language)
    # Count syllables for each word.
    syllable_counts = [dic.inserted(word).count('-') + 1 for word in words if word]
    return sum(syllable_counts)


def avg_syllables_per_word(text, language):
    words = text.split()
    if not words:
        return 0
    dic = get_pyphen(language)
    syllable_counts = [dic.inserted(word).count('-') + 1 for word in words if word]
    return sum(syllable_counts) / len(syllable_counts) if syllable_counts else 0


def count_words(doc):
    # Count tokens that are not punctuation.
    return len([token for token in doc if not token.is_punct])


def count_sentences(doc):
    return len(list(doc.sents))


def count_unique_words(doc):
    return len(set(token.text.lower() for token in doc if not token.is_punct))


def lexical_diversity(doc):
    words = [token for token in doc if not token.is_punct]
    if not words:
        return 0
    return count_unique_words(doc) / len(words)


def average_pos(doc):
    # List of universal POS tags.
    all_pos_tags = [
        "ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", "NOUN", "NUM",
        "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE",
    ]
    pos_counts = {pos: 0 for pos in all_pos_tags}
    for token in doc:
        if token.pos_ in pos_counts:
            pos_counts[token.pos_] += 1
    doc_length = len(doc) if len(doc) > 0 else 1  # Prevent division by zero.
    return {pos: count / doc_length for pos, count in pos_counts.items()}


def calculate_readability(text, language):
    textstat.set_lang(language)
    return {
        'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
        'smog_index': textstat.smog_index(text),
        'coleman_liau_index': textstat.coleman_liau_index(text),
        'automated_readability_index': textstat.automated_readability_index(text),
        'dale_chall_readability_score': textstat.dale_chall_readability_score(text),
        'difficult_words': textstat.difficult_words(text),
        'linsear_write_formula': textstat.linsear_write_formula(text),
        'gunning_fog': textstat.gunning_fog(text)
    }


def predict_sentiment_prob(text, sentiment_model, language):
    if not sentiment_model:
        return {"positive": None, "neutral": None, "negative": None}
    if language == "en":
        result = sentiment_model.polarity_scores(text)
        return {"positive": result["pos"], "negative": result["neg"], "neutral": result["neu"]}
    elif language == "de":
        result = sentiment_model.predict_sentiment([text], output_probabilities=True)
        # Adjust this if the sentiment model output format changes.
        return dict(result[1][0])
    else:
        raise ValueError("Language not supported. Supported languages are: 'en' and 'de'.")


def extract_abstractness_features(doc, abstractness_lookup, language, stopword_list):
    """
    For each token, if its lowercased lemma is in the abstractness lookup and is not a stopword,
    use its abstractness scores. Otherwise, use zeros.
    """
    abs_keys = {"en": ["Conc.M"], "de": ['AbstConc', 'Arou', 'IMG', 'Val']}
    # If no abstractness data is available, return zeros.
    if abstractness_lookup is None:
        return {key: 0 for key in abs_keys.get(language, [])}

    score_list = []
    for tok in doc:
        lemma = tok.lemma_.lower()
        # Compare lower-case token text with stopwords.
        if lemma not in stopword_list and lemma in abstractness_lookup:
            abs_data = abstractness_lookup[lemma]
            score_list.append({k: abs_data.get(k, 0) for k in abs_keys[language]})
    if not score_list:
        score_list.append({k: 0 for k in abs_keys[language]})
    # Compute the mean of each abstractness feature over the tokens.
    cdf = pd.DataFrame(score_list)[abs_keys[language]].mean().to_dict()
    return cdf
def extract_named_entities(doc):
    # Define categories and count occurrences using generator expressions.
    people_entities = {'PERSON', 'PER'}
    temporal_entities = {'TIME', 'DATE', 'EVENT'}
    spatial_entities = {'GPE', 'LOC', 'FAC'}
    quantity_entities = {'PERCENT', 'MONEY', 'QUANTITY', 'CARDINAL', 'ORDINAL'}

    people_counter = sum(1 for ent in doc.ents if ent.label_ in people_entities)
    temporal_counter = sum(1 for ent in doc.ents if ent.label_ in temporal_entities)
    spatial_counter = sum(1 for ent in doc.ents if ent.label_ in spatial_entities)
    quantity_counter = sum(1 for ent in doc.ents if ent.label_ in quantity_entities)

    return {
        "people_entities": people_counter,
        "temporal_entities": temporal_counter,
        "spatial_entities": spatial_counter,
        "quantity_entities": quantity_counter
    }


def get_declarative_stylometric_features(liwc_data, language):
    # Calculate combined LIWC features.
    liwc_data['self_reference'] = liwc_data['i'] + liwc_data['we']

    if language == "de":
        liwc_data['other_reference'] = liwc_data['shehe'] + liwc_data['they'] + liwc_data['you_total']
        liwc_data['perceptual_details'] = (liwc_data['percept'] + liwc_data['see'] +
                                           liwc_data['hear'] + liwc_data['feel'])
        liwc_data['contextual_embedding'] = liwc_data['space'] + liwc_data['motion'] + liwc_data['time']
        liwc_data['reality_monitoring'] = (liwc_data['contextual_embedding'] +
                                           liwc_data['perceptual_details'] +
                                           liwc_data['affect'] - liwc_data['cogproc'])
    else:
        liwc_data['other_reference'] = liwc_data['shehe'] + liwc_data['they'] + liwc_data['you']
        liwc_data['perceptual_details'] = (liwc_data['attention'] + liwc_data['auditory'] +
                                           liwc_data['visual'] + liwc_data['feeling'])
        liwc_data['contextual_embedding'] = liwc_data['space'] + liwc_data['motion'] + liwc_data['time']
        liwc_data['reality_monitoring'] = (liwc_data['contextual_embedding'] +
                                           liwc_data['perceptual_details'] +
                                           liwc_data['Affect'] - liwc_data['Cognition'])
    return liwc_data
