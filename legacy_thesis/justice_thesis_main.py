from feature_extraction import (
    load_resources,
    count_words,
    count_sentences,
    count_syllables,
    avg_syllables_per_word,
    lexical_diversity,
    average_pos,
    calculate_readability,
    predict_sentiment_prob,
    extract_named_entities,
    extract_abstractness_features,
    get_declarative_stylometric_features
)
from utils import read_csv, write_csv
import pandas as pd
from tqdm import tqdm
import argparse


def process_text_data(input_csv, liwc_analysis_included, text_column, language, output_csv):
    # Load language-specific resources once.
    nlp, abstractness_lookup, sentiment_model, stopword_list = load_resources(language)

    data = read_csv(input_csv)
    features = []

    # Iterate over the texts with a progress bar.
    for text in tqdm(data[text_column].astype(str), desc="Processing Text"):
        doc = nlp(text)
        row = {
            'word_count': count_words(doc),
            'sentence_count': count_sentences(doc),
            'syllable_count': count_syllables(text, language),
            'avg_syllables_per_word': avg_syllables_per_word(text, language),
            'lexical_diversity': lexical_diversity(doc),
            **average_pos(doc),
            **calculate_readability(text, language),
            **predict_sentiment_prob(text, sentiment_model, language),
            **extract_named_entities(doc),
            **extract_abstractness_features(doc, abstractness_lookup, language, stopword_list),
        }
        features.append(row)

    features_df = pd.DataFrame(features)
    # Join the features with the original data.
    features_df = data.join(features_df)
    if liwc_analysis_included:
        features_df = get_declarative_stylometric_features(features_df, language)

    write_csv(features_df, output_csv)


def main():
    parser = argparse.ArgumentParser(description="Process text data from a CSV file.")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument(
        "--liwc_analysis_included",
        action="store_true",
        help="Flag indicating whether the input file contains LIWC analysis"
    )
    parser.add_argument("--text_column", required=True, help="Name of the column with text data")
    parser.add_argument("--language", required=True, help="Language of the text (e.g., 'de', 'en')")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    process_text_data(
        args.input,
        args.liwc_analysis_included,
        args.text_column,
        args.language,
        args.output
    )


if __name__ == "__main__":
    main()
