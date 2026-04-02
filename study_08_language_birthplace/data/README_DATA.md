# Data Sources — Study 8: Language & Birthplace

## Overview

This study uses **hardcoded census proportions** from 8 countries. No external data download is required — all values are embedded in `src/run.py`.

## Sources

| Country | Source | Year | Population | % Dominant Language |
|---------|--------|------|------------|-------------------|
| Australia | ABS Census | 2021 | 25,422,788 | 72.0% English |
| Canada | Statistics Canada | 2021 | 36,991,981 | 96.9% English/French |
| China | National Bureau of Statistics | 2020 | 1,411,778,724 | 92.0% Mandarin |
| France | INSEE | 2021 | 67,390,000 | 91.2% French |
| Germany | Destatis | 2021 | 82,700,000 | 81.0% German |
| Mexico | INEGI Census | 2020 | 126,014,024 | 93.8% Spanish |
| New Zealand | Stats NZ Census | 2018 | 4,699,755 | 95.4% English |
| United Kingdom | ONS Census | 2021 | 56,490,048 | 91.1% English |

**Total N = 1,811,487,320**

## Notes

- "Dominant language" means the most widely spoken language at home
- Australia's lower percentage (72%) reflects its higher immigration rate and multicultural language policy
- All percentages are from official national census data
- The null hypothesis tested is that language is independent of birthplace (50/50 chance), which all countries reject with p < .001
