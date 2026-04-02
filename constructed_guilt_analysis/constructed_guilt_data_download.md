# Corpus Data Download Instructions

## Cross-Cultural Deception (Perez-Rosas & Mihalcea, 2014)

**Status:** Partially present in `data/raw/crossCulturalDeception.2014/`

Some files are missing from the local copy. To get the complete corpus:

```bash
cd data/raw/
curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/crossCulturalDeception.2014.tar.gz" -o crossCultural.tar.gz
tar -xzf crossCultural.tar.gz
```

This should give you the full dataset with all 4 cultures (US, India, Mexico, Romania)
across 3 topics (abortion, best friend, death penalty), with both truthful and deceptive
essays.

**Expected file counts per README:**

| Dataset       | Abortion | BestFriend | Death Penalty |
|---------------|----------|------------|---------------|
| EnglishUS     | 100      | 100        | 100           |
| EnglishIndia  | 100      | 100        | 100           |
| SpanishMexico | 39       | 94         | 42            |
| Romanian      | 139      | 151        | 145           |

Each count is per-label (truthful + deceptive), so total essays = 2x the above.

**Currently missing locally:**
- EnglishIndia: abortion.True, abortion.False, bestFriend.True, deathPenalty.False
- EnglishUS: bestFriend.False
- SpanishMexico: abortion.False, deathPenalty.True

## Open-Domain Deception (Perez-Rosas & Mihalcea, 2015)

**Status:** Not present locally.

```bash
mkdir -p data/openDomain/
curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/openDeception.2015.tar.gz" -o openDeception.tar.gz
tar -xzf openDeception.tar.gz -C data/openDomain/
```

512 users, 7 lies + 7 truths each, with demographic data (gender, age, country, education).

## Source

Veronica Perez-Rosas and Rada Mihalcea
Language and Information Technologies, University of Michigan
https://web.eecs.umich.edu/~mihalcea/downloads/
