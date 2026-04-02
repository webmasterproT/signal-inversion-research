Multilingual Deception Datasets
English (India and US), Spanish, and Romanian
=============================================

Veronica Perez-Rosas and Rada Mihalcea
Language and Information Technologies
University of Michigan

vrncapr@umich.edu
mihalcea@umich.edu

Version 1.0
November 2014



1. Introduction

This document describes the datasets used in the paper Cross-cultural Deception Detection (Perez-Rosas and Mihalcea, 2014).

2. Datasets information

The English datasets were collected from English speakers using Amazon Mechanical Turk. The Spanish and Romanian datasets were collected from native Spanish and Romanian speakers using a web interface. Each dataset consists of short deceptive and truthful essays for three topics: opinions on Abortion, opinions on Death Penalty, and feelings about a Best Friend. 

3. Dataset structure

The main directory contains two deception datasets in English, one deception dataset in Spanish, and one in Romanian labeled as follows:
- EnglishUS 
- EnglishIndia
- SpanishMexico
- Romanian

Each dataset contains short truthful and deceptive essays for three different topics: abortion (ab), best friend (bf), death penalty (dp). Both deceptive and truthful statements are provided in two separated text files and contain an id and a single statement per line. 

The data distribution is as follows:

+---------------+---------------------------------------+
|               |                 Topic                 |
+       Dataset +---------------------------------------+
|               | Abortion | BestFriend | Death Penalty |
+---------------+----------+------------+---------------+
| EnglishUS     |    100   |     100    |      100      |
+---------------+----------+------------+---------------+
| EnglishIndia  |    100   |     100    |      100      |
+---------------+----------+------------+---------------+
| SpanishMexico |    39    |     94     |       42      |
+---------------+----------+------------+---------------+
| Romanian      |    139   |     151    |      145      |
+---------------+----------+------------+---------------+


4. Feedback

For further questions or inquiries about this dataset, you can contact: Veronica Perez-Rosas (vrncapr@umich.edu) or Rada Mihalcea (mihalcea@umich.edu).


5. Citation Information

If you use this dataset, please cite:

@Proceedings{Perez14,
author="P{\'e}rez-Rosas, Ver{\'o}nica and Mihalcea, Rada",
title="Cross-cultural Deception Detection",
series="Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
year="2014",
publisher="Association for Computational Linguistics",
pages="440--445",
location="Baltimore, Maryland",
url="http://aclweb.org/anthology/P14-2072"
}


6. Acknowledgements

This material is based in part upon work supported by National Science Foundation awards numbers 1344257 and 1355633 and by DARPA-BAA-12-47 DEFT grant number 12475008. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation or the Defense Advanced Research Projects Agency.
