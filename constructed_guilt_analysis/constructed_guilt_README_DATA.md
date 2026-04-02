# Data Directory

## Real Datasets

The analysis runs on demo data out of the box. To use the real datasets, download them here:

### 1. Cross-Cultural Deception (Pérez-Rosas & Mihalcea, 2014)

US, India, Mexico, Romania — essays on abortion, death penalty, best friend.
~100 statements per culture, truthful and deceptive.

```bash
curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/crossCulturalDeception.2014.tar.gz" -o crossCultural.tar.gz
tar -xzf crossCultural.tar.gz -C data/crossCultural/
```

Expected layout after extraction:
```
data/crossCultural/
    US/
        abortion/  lies/ truths/
        death_penalty/ ...
        best_friend/ ...
    India/
    Mexico/
    Romania/
```

### 2. Open-Domain Deception (Pérez-Rosas & Mihalcea, 2015)

512 users, 7 lies + 7 truths each, with demographic data (country, gender, age, education).

```bash
curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/openDeception.2015.tar.gz" -o openDeception.tar.gz
tar -xzf openDeception.tar.gz -C data/openDomain/
```

Expected layout after extraction:
```
data/openDomain/
    deception_data.csv   OR
    lies/  + truths/     OR
    users/ with per-user files
```

## Demo Data

If neither dataset is found, the script generates synthetic data with realistic cross-cultural parameters derived from published LIWC norms. The demo data produces the same directional pattern as the real data and validates the full analysis pipeline.

Culture parameters (hedging rate h, certainty rate c — per 100 words):
- US: h=3.2, c=2.1 (Anglo direct style)
- India: h=5.1, c=1.4 (deference norms in English)
- Mexico: h=2.8, c=3.3
- Romania: h=1.9, c=2.8 (formal assertion style)

40 speakers per culture x 2 conditions (truthful/deceptive) = 320 statements.
