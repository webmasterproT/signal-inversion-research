# Data Sources — Study 9: Environmental Outcomes

## Required Data

This study requires the US Census American Community Survey (ACS) Public Use Microdata Sample (PUMS) for California, 2022.

**File:** `psam_p06.csv` (~263 MB)

### Download Instructions

1. Go to https://www.census.gov/programs-surveys/acs/microdata/access.html
2. Select "2022 ACS 1-Year PUMS"
3. Download the **Person** file for **California** (state code 06)
4. Direct FTP link: `https://www2.census.gov/programs-surveys/acs/data/pums/2022/1-Year/csv_pca.zip`
5. Extract `psam_p06.csv` and place it in this `data/` directory

### Key Variables Used

| Variable | Description | Values |
|----------|-------------|--------|
| AGEP | Age | 0-99 |
| SCHL | Educational attainment | 1-24 (21+ = Bachelor's or higher) |
| LANX | Language at home | 1=English only, 2=Other |
| LANP | Detailed language code | Various |
| ANC1P | First ancestry code | 1-999 |
| NATIVITY | Native/foreign born | 1=Native, 2=Foreign |
| WAGP | Wage/salary income | Dollars |

### Demo Mode

If the census file is not available, the script automatically runs in **demo mode** with synthetic data (N=50,000) that mimics the real data's structure and approximate distributions. To force demo mode:

```bash
python src/run.py --demo
```

Demo mode results demonstrate the analysis pipeline but should not be cited. Only results from the real census data are publication-quality.

## Citation

US Census Bureau. (2023). American Community Survey 2022 1-Year Public Use Microdata Sample. Retrieved from https://www.census.gov/programs-surveys/acs/microdata.html
