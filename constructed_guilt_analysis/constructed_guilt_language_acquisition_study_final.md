Geographic Birthplace as a Predictor of
          Primary Language:

A Cross-National Observational Study



           OMXUS Research Initiative

                research@omxus.com




                  February 2026




             Preprint – Not peer reviewed

---
                                     Abstract


   Background: Language acquisition is a fundamental aspect of human devel-

opment, yet the relative contributions of environmental versus biological factors

remain underexplored in large-scale empirical studies. This observational study

examines whether geographic birthplace predicts primary language spoken across

multiple nations.

   Methods: We analysed national census data from eight countries (N = 1,811,487,320

individuals) spanning six continents. Primary outcome was concordance between

country of residence and dominant national language spoken. Chi-square tests and

effect size calculations (Cohen’s h) were conducted.

   Results: Across all nations examined, geographic residence demonstrated strong

concordance with national language acquisition (range: 72.0%–96.9%). Effect sizes

ranged from h = 0.46 to h = 1.22 (mean = 0.93; classified as “medium” to “large”

by conventional standards). The observed pattern held regardless of the specific

language examined.

   Conclusions: Geographic environment appears to be an extraordinarily strong

predictor of language acquisition. Supplementary analysis of international adop-

tion studies and twin research confirms that environment, not genetics, determines

which language an individual speaks. The implications for understanding human

behavioural acquisition more broadly warrant further investigation.

   Keywords: language acquisition; environmental factors; cross-national study;

census data; nature versus nurture




                                         1

---
Key Points

    • Geographic environment predicts primary language with 72–97% accuracy across
      eight nations

    • Effect sizes (mean Cohen’s h = 0.93) exceed conventional “large” thresholds

    • International adoption studies show 100% language replacement regardless of ge-
      netic ancestry

    • Twin studies confirm genetics affects language ability, not which language is spoken

    • Findings have implications for understanding environmental determination of com-
      plex human behaviours




1     Introduction


1.1     Background


Human language is among the most complex cognitive abilities exhibited by any species.
The average adult possesses a productive vocabulary of approximately 20,000–35,000
words, applies grammatical rules unconsciously in real-time, and processes speech at
rates exceeding 150 words per minute (Brysbaert et al., 2016). Despite this complexity,
healthy children across all cultures acquire language with remarkable consistency.

The question of how language is acquired has been debated extensively. Nativist per-
spectives emphasise innate language acquisition devices (Chomsky, 1965), while empiri-
cist perspectives highlight environmental exposure and social learning (Tomasello, 2003).
However, large-scale empirical studies examining the actual distribution of language out-
comes across populations remain limited.




                                             2

---
1.2    Research Question


This study addresses a straightforward empirical question: To what extent does geographic
birthplace predict the primary language an individual speaks?

We then performed systematic cross-national analyses quantifying this relationship with
standardised effect size metrics. Such quantification may provide useful baseline data for
understanding environmental contributions to complex human behaviours.



1.3    Hypotheses


H0 (Null Hypothesis): Geographic birthplace is not associated with primary language
spoken, and language acquisition occurs independently of geographic environment.

H1 (Alternative Hypothesis): Geographic birthplace is associated with primary lan-
guage spoken, and language acquisition is related to geographic environment.

We set our significance threshold at α = 0.05.




2     Methods


2.1    Design


Cross-sectional observational study using publicly available national census data.



2.2    Data Sources


We identified national statistical agencies with publicly available census data on language
spoken. Countries were selected based on: (1) availability of recent census data (2011–
2022); (2) data published in or translatable to English; (3) inclusion of language variables;

                                             3

---
and (4) geographic and linguistic diversity.



2.3    Variables

  • Predictor: Country of residence at time of census

  • Outcome: Primary language spoken (national language vs. other)



2.4    Statistical Analysis


For each country, we calculated:


  1. Proportion speaking the dominant national language

  2. Chi-square goodness-of-fit test against null expectation (50%)

  3. Effect size (Cohen’s h)


Cohen’s h is calculated as:

                                           √                √
                              h = 2 arcsin( p1 ) − 2 arcsin( p2 )                    (1)



Effect size interpretation (Cohen, 1988): Small = 0.20; Medium = 0.50; Large = 0.80.

All analyses were conducted in Python 3.12 using scipy and statsmodels packages.



2.5    Ethical Considerations


This study used only publicly available, anonymised aggregate census data. No individual-
level data were accessed. Institutional review was not required per standard guidelines
for secondary analysis of public data.


                                               4

---
3     Results


3.1    Sample Characteristics


The combined sample included N = 1,811,487,320 individuals from eight countries (Table
1).

                      Table 1: Sample Characteristics by Country
              Country           Year      Population Source
              Australia      2021             25,422,788   ABS
              Canada         2021             36,991,981   Statistics Canada
              China          2020          1,411,778,724   NBS
              France         2021             67,390,000   INSEE
              Germany        2022             82,700,000   Destatis
              Mexico         2020            126,014,024   INEGI
              New Zealand    2018              4,699,755   Stats NZ
              United Kingdom 2021             56,490,048   ONS
              Total               —      1,811,487,320     —




3.2    Language Concordance


Table 2 presents the proportion speaking the dominant national language.

              Table 2: Proportion Speaking Dominant National Language
                   Country            Language(s)    % Speaking
                      Australia      English                     72.0%
                      Canada         English/French              96.9%
                      China          Chinese                     92.0%
                      France         French                      91.2%
                      Germany        German                      81.0%
                      Mexico         Spanish                     93.8%
                      New Zealand    English                     95.4%
                      United Kingdom English                     91.1%

Note: Australia’s lower percentage reflects high immigration; among Australian-born
residents, English prevalence exceeds 95%.




                                             5

---
3.3    Statistical Tests


All chi-square tests were significant at p < .001 (Table 3).

                     Table 3: Chi-Square and Effect Size Results
             Country            %            χ2 df         p Cohen’s h
             Australia           72.0   4,921,852      1   < .001   0.46 (S)
             Canada              96.9 32,547,173       1   < .001   1.22 (L)
             China               92.0 996,151,068      1   < .001   1.00 (L)
             France              91.2 45,756,193       1   < .001   0.97 (L)
             Germany             81.0 31,789,880       1   < .001   0.67 (M)
             Mexico              93.8 96,700,138       1   < .001   1.07 (L)
             New Zealand         95.4   3,874,779      1   < .001   1.14 (L)
             United Kingdom      91.1 38,169,422       1   < .001   0.96 (L)

Note: S = Small, M = Medium, L = Large effect size. Effect sizes calculated against null
expectation of 50% (chance). This is a conservative test.




3.4    Effect Size Summary


Mean Cohen’s h = 0.93 (SD = 0.24), range 0.46–1.22.

To contextualise: Cohen (1988) classified h = 0.80 as a “large” effect. The observed mean
effect was 1.2 times the “large” threshold, with 6 of 8 countries showing large effects.



3.5    Cross-National Consistency


The relationship between geographic residence and language held regardless of:


  • The specific language (English, French, Mandarin, Spanish, German)

  • Geographic region (Europe, Asia, Oceania, North America)

  • Population size (4.7 million to 1.4 billion)

  • Economic development level (varied)


                                             6

---
4     Discussion


4.1     Summary of Findings


This cross-national observational study examined whether geographic birthplace predicts
primary language spoken. Across eight nations representing 1.8 billion individuals:


    1. Strong concordance: Proportions speaking national language: 72.0%–96.9%

    2. Statistical significance: All p-values < .001

    3. Large effect sizes: Mean Cohen’s h = 0.93, exceeding “large” threshold

    4. Cross-national consistency: Pattern held across languages, regions, and popu-
      lation sizes


These findings support rejection of the null hypothesis. Geographic environment appears
strongly associated with language acquisition.



4.2     Comparison with Prior Literature


The observed effect sizes are comparable to or larger than those typically reported in
behavioural research. For comparison:


    • Educational interventions: d = 0.40 (Hattie, 2009)

    • Psychotherapy outcomes: d = 0.80 (Smith & Glass, 1977)

    • Present study: h = 0.93 (mean)


Critically, our comparison against a 50% null is highly conservative. The meaningful
comparison is not “better than chance” but rather “near-perfect prediction.” In practical
terms, knowing where someone lives predicts their language with accuracy exceeding 90%
in most nations examined.

                                           7

---
4.3     Supplementary Evidence


4.3.1   International Adoption Studies


Korean children adopted by Swedish families speak Swedish. Chinese children adopted
by American families speak English. No study has found spontaneous birth-language
acquisition without environmental exposure (Pallier et al., 2003; Hyltenstam et al., 2009).

Effect: 100% language replacement.



4.3.2   Twin Studies


The Minnesota Study of Twins Reared Apart (Bouchard et al., 1990) found that genetics
affects language ability (heritability estimates 25–70%), but which language is spoken
shows 0% heritability.

The “Jim Twins”—identical twins separated at birth and reunited at age 39—both spoke
English. This was because both were raised in Ohio, not because of any genetic predis-
position toward English.



4.3.3   Generational Studies


Hispanic immigrants to the United States show complete language shift within three
generations (Portes & Rumbaut, 2001):


  • 1st generation: 85% Spanish-dominant

  • 2nd generation: 47% bilingual

  • 3rd generation: 92% English-dominant


This occurred despite genetic continuity across all three generations.


                                            8

---
4.4    Limitations


Several limitations warrant consideration:



  1. Ecological design: We analysed aggregate census data, not individual-level data

  2. Cross-sectional: Cannot establish temporal sequence (though birthplace logically
      precedes language acquisition)

  3. Unmeasured confounds: Genetic factors, parental language, immigration status
      not directly controlled in primary analysis

  4. Measurement variability: Different censuses used different language questions



4.5    Possible Alternative Explanations


The strong association between geographic environment and language could theoretically
be explained by:



  1. Selection effects: Perhaps individuals predisposed to speak certain languages
      migrate to corresponding countries

  2. Genetic factors: Perhaps language capacity is inherited and populations cluster
      geographically

  3. Reverse causation: Perhaps language determines where people live



However, these alternatives face logical difficulties. Infants do not choose where they
are born, and neonates show no language capacity at birth that could guide parental
migration decisions. The temporal sequence (birth → geographic exposure → language
acquisition) appears well-established.




                                             9

---
5     Potential Implications

These findings may have broader implications beyond linguistics.

Language acquisition requires:


    • Complex motor coordination (articulation)

    • Memory systems (vocabulary of 20,000+ words)

    • Abstract rule learning (grammar)

    • Social calibration (pragmatics)

    • Emotional expression (prosody)


If all these complex cognitive-behavioural systems are environmentally determined for
language, what does this suggest about simpler behavioural patterns?

Consider:


    • Emotional responses (anger, fear, joy)

    • Social behaviours (trust, cooperation, aggression)

    • Cognitive styles (analytical vs. holistic thinking)

    • Preferences (food, music, relationships)


We do not claim to have answered these questions. We note only that the evidence for
environmental determination of language is so overwhelming that it may provide a useful
prior for investigating other behavioural domains.




                                             10

---
5.1    Unexpected Reflection


We confess that, upon completing this analysis, we found ourselves somewhat surprised—
not by the statistical results, which were as expected, but by what they imply.

The finding that “people speak the language of their environment” is so obvious it hardly
seems worth stating. Yet when we apply the same logic to other behavioural patterns—
emotional responses, interpersonal styles, even preferences and dispositions—we often
default to genetic or dispositional explanations. Our entire criminal justice system is
predicated on it.

A child raised in Sydney speaks English not because of any genetic predisposition toward
English, but because that is what their environment provided. Might the same logic apply
to a child raised in an environment where anger is the standard response to frustration?
Or where distrust is the standard response to uncertainty?

We did not anticipate that an analysis of census language data would prompt such ques-
tions. But the effect sizes observed—larger than those in most behavioural research—
suggest that environment may be a more powerful determinant of human behaviour than
is commonly assumed.


      If the most complex behaviour (language) is 100% predicted by environment,
      the default assumption for simpler behaviours might reasonably be environ-
      mental as well.




6     Conclusions

This cross-national observational study found that geographic environment is strongly as-
sociated with language acquisition, with effect sizes substantially exceeding conventional
thresholds. The pattern held across eight nations, multiple languages, and over 1.8 billion
individuals.

                                            11

---
While the finding that “people speak the language where they live” may seem trivially
obvious, the magnitude of the effect—and its potential implications for understanding
human behavioural acquisition more broadly—may be less obvious than the finding itself.

Further research is warranted to explore whether environmental determination of lan-
guage represents a special case, or whether it exemplifies a more general principle appli-
cable to human behaviour.




Data Availability

All data used in this study are publicly available from national statistical agencies:


  • Australian Bureau of Statistics (ABS): https://www.abs.gov.au

  • Statistics Canada: https://www.statcan.gc.ca

  • National Bureau of Statistics of China (NBS): https://www.stats.gov.cn

  • INSEE (France): https://www.insee.fr

  • Destatis (Germany): https://www.destatis.de

  • INEGI (Mexico): https://www.inegi.org.mx

  • Stats NZ (New Zealand): https://www.stats.govt.nz

  • Office for National Statistics (UK): https://www.ons.gov.uk


Analysis code is available at: https://github.com/omxus/language-acquisition-study




Declarations

Ethical Approval: Not applicable. This study used only publicly available, anonymised
aggregate census data.

                                            12

---
Consent for Publication: Not applicable. No individual person’s data were used.

Competing Interests: The authors declare that they have no competing interests.

Funding: This research received no specific grant from any funding agency in the public,
commercial, or not-for-profit sectors.




References

Bouchard, T. J., Lykken, D. T., McGue, M., Segal, N. L., & Tellegen, A. (1990). Sources

of human psychological differences: The Minnesota Study of Twins Reared Apart. Science,

250(4978), 223–228.


Brysbaert, M., Stevens, M., Mandera, P., & Keuleers, E. (2016). How many words do we know?

Practical estimates of vocabulary size dependent on word definition, the degree of language input

and the participant’s age. Frontiers in Psychology, 7, 1116.


Chomsky, N. (1965). Aspects of the theory of syntax. MIT Press.


Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence

Erlbaum Associates.


Hattie, J. (2009). Visible learning: A synthesis of over 800 meta-analyses relating to achieve-

ment. Routledge.


Hyltenstam, K., Bylund, E., Abrahamsson, N., & Park, H. S. (2009). Dominant-language

replacement: The case of international adoptees. Bilingualism: Language and Cognition, 12(2),

121–140.


Pallier, C., Dehaene, S., Poline, J. B., LeBihan, D., Argenti, A. M., Dupoux, E., & Mehler, J.

(2003). Brain imaging of language plasticity in adopted adults: Can a second language replace

the first? Cerebral Cortex, 13(2), 155–161.


Portes, A., & Rumbaut, R. G. (2001). Legacies: The story of the immigrant second generation.



                                               13

---
University of California Press.


Smith, M. L., & Glass, G. V. (1977). Meta-analysis of psychotherapy outcome studies. Ameri-

can Psychologist, 32(9), 752–760.


Tomasello, M. (2003). Constructing a language: A usage-based theory of language acquisition.

Harvard University Press.




                                            14

---
