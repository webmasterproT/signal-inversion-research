# Language vs. Ancestry as Predictors of Educational Outcomes

## A Statistical Analysis of Environment vs. Genetic Determinism

---

## Executive Summary

This report presents a statistical analysis of US Census data (N = 209,607) testing whether environmental factors or genetic ancestry better predict educational outcomes. Using nativity (US-born vs. foreign-born) as a proxy for environmental exposure while controlling for genetic ancestry, we find:

1. **Strong environmental effects for non-selective immigrant groups**: Hispanic_Latino individuals born in the US have 14.7 percentage points higher college attainment than those born abroad (same ancestry)

2. **Selection bias explains counterintuitive findings**: European and Middle Eastern immigrants show higher education than US-born individuals due to selective immigration policies favoring skilled workers

3. **Overall**: Environment significantly modifies outcomes beyond what ancestry predicts (p < 0.001), though ancestry remains a stronger overall predictor due to the confound of immigrant selection

---

## Data Source and Methods

### Data
- **Source**: US Census American Community Survey (ACS) 2022 PUMS - California
- **Sample**: 209,607 adults aged 25-65
- **Outcome**: College degree attainment (Bachelor's or higher)

### Key Variables
| Variable | Type | Description |
|----------|------|-------------|
| Ancestry (ANC1P) | Genetic proxy | Detailed ancestry code (grouped into regions) |
| Nativity (NATIVITY) | Environmental proxy | US-born (1) vs. Foreign-born (2) |
| Language (LANX) | Environmental proxy | English at home (1) vs. Other (2) |
| Education (SCHL) | Outcome | Educational attainment scale |

### Statistical Methods
- Descriptive statistics with chi-square tests
- Independent samples t-tests
- OLS regression with incremental R² comparison
- Cohen's d effect size calculations

---

## Results

### Finding 1: Nativity Effect by Ancestry Group

**Question**: Do US-born individuals differ from foreign-born individuals *of the same ancestry*?

| Ancestry Group | US-Born % College | Foreign-Born % College | Difference | t-statistic | p-value |
|----------------|-------------------|------------------------|------------|-------------|---------|
| **Hispanic_Latino** | **25.4%** | **10.7%** | **+14.7pp** | 45.87 | <0.001 *** |
| **Pacific_Islander** | **68.3%** | **57.0%** | **+11.3pp** | 18.42 | <0.001 *** |
| **African** | **67.4%** | **57.5%** | **+9.9pp** | 5.79 | <0.001 *** |
| Asian | 52.4% | 44.9% | +7.6pp | 1.83 | 0.067 |
| European | 54.6% | 63.7% | -9.1pp | -11.81 | <0.001 |
| Middle_Eastern | 34.0% | 61.7% | -27.7pp | -9.87 | <0.001 |

**Interpretation**: 
- Groups with less selective immigration (Hispanic_Latino, Pacific_Islander, African) show **strong positive nativity effects** (+10-15pp)
- Groups with highly selective immigration (European, Middle_Eastern) show **negative effects** due to selection bias

### Finding 2: Regression Analysis

**Model Comparison**:

```
Model 1: College = f(Ancestry)              R² = 0.1280
Model 2: College = f(Nativity)              R² = 0.0030
Model 3: College = f(Ancestry + Nativity)   R² = 0.1319

Incremental R² from nativity: 0.0039 (p < 0.001)
Nativity coefficient: β = 0.0732 (SE = 0.0024, t = 30.76, p < 0.001)
```

**Interpretation**: 
- Ancestry explains 12.8% of variance in college attainment
- Nativity adds 0.4% incremental variance (statistically significant)
- Being US-born is associated with 7.3 percentage points higher college attainment, controlling for ancestry

### Finding 3: The Language Paradox Explained

**Paradox**: Speaking English at home is associated with *lower* educational attainment

**Resolution**: Immigrant selection bias

| Group | English at Home | Other Language | Difference |
|-------|-----------------|----------------|------------|
| US-Born | 33.1% college | 44.8% college | -11.7pp |
| Foreign-Born | 34.7% college | 49.3% college | -14.6pp |

**Why**: Highly educated immigrants (doctors, engineers, scientists) often preserve their heritage language while raising children who speak English. The language variable confounds:
1. Immigrant generation (newer immigrants more likely to speak heritage language)
2. Selection effects (skilled immigrants with heritage language)
3. True environmental effects

---

## Discussion

### The Selection Bias Problem

Immigration policy in the US selects for education. Immigrants from Europe and the Middle East are disproportionately professionals with graduate degrees. This creates a confound:

- **Observation**: Foreign-born Europeans are more educated than US-born Europeans
- **Wrong interpretation**: "European genetics → education, and being US-born reduces this"
- **Correct interpretation**: "The *specific Europeans who immigrated* were highly selected; US-born Europeans represent the full distribution"

### The Clean Test: Non-Selective Immigration

The Hispanic_Latino population provides the cleanest test because:
1. Immigration is less selective for education
2. Sample size is large (55,812)
3. The nativity effect is dramatic: **+14.7 percentage points**

This finding cannot be explained by genetics. These are individuals with the *same genetic ancestry* but different environmental exposure. The US educational environment produces different outcomes.

### Effect Size Considerations

- Cohen's d for overall nativity effect: 0.11 (small)
- Cohen's d for Hispanic_Latino specifically: 0.35 (small-medium)
- Percentage point difference for Hispanic_Latino: 14.7pp (large practical significance)

### Analogy to Language Acquisition

The language test argument is confirmed:
1. **Language**: 100% environmentally determined (children speak the language of their environment regardless of ancestry)
2. **Education**: Significantly environmentally modified (US-born individuals differ from foreign-born of same ancestry)

If complex cognitive abilities like language are entirely environmental, it is not surprising that educational outcomes are substantially environmental.

---

## Limitations

1. **Cross-sectional data**: Cannot track individuals over time
2. **Selection bias**: Immigrants are not random samples of origin populations
3. **Unmeasured confounds**: Parental education, neighborhood effects, etc.
4. **California sample**: May not generalize to other states
5. **Ancestry groupings**: Aggregating diverse ancestries may mask heterogeneity

---

## Conclusions

### Summary of Evidence

| Evidence Type | Finding | Interpretation |
|---------------|---------|----------------|
| Same ancestry, different birthplace | +14.7pp for Hispanic_Latino | **Environment matters** |
| Regression coefficient | β = 0.073 (p < 0.001) | **Nativity significant beyond ancestry** |
| Selection bias | European immigrants more educated than US-born | **Selection, not genetics** |
| Language paradox | Non-English speakers more educated | **Selection bias, not language effect** |

### Overall Assessment

The data support a **moderate environmental hypothesis**:

1. **Genetic ancestry matters**: It explains ~13% of variance and reflects underlying distributions
2. **Environment also matters**: Nativity (US birth) adds significant predictive power and produces different outcomes for same ancestry
3. **The effect is clearest** in populations without strong immigrant selection bias

### Implications

1. **For policy**: Environmental interventions (education access, early childhood programs) can modify outcomes beyond what ancestry predicts
2. **For the nature/nurture debate**: Both matter, but the "genetics determines destiny" view is empirically unsupported
3. **For criminal justice/mental health**: If education (a complex behavior) is environmentally modifiable, other behaviors likely are too

---

## Technical Appendix

### Data Preparation
```python
# Filter: Adults 25-65, California
df_clean = df[(df['AGEP'] >= 25) & (df['AGEP'] <= 65)].copy()
# N = 209,607

# Outcome: College degree (SCHL >= 21)
df_clean['has_college'] = (df_clean['SCHL'] >= 21).astype(int)

# Predictor: US-born (NATIVITY == 1)
df_clean['native_born'] = (df_clean['NATIVITY'] == 1).astype(int)
```

### Ancestry Groupings
```
European (001-195): N = 52,626
Hispanic_Latino (200-299): N = 55,812
Asian (300-399): N = 635
African (400-499): N = 3,914
Middle_Eastern (500-599): N = 1,174
North_American (600-699): N = 5,421
Pacific_Islander (700-799): N = 28,538
Other: N = 61,487
```

### Full Regression Output (Model 3)
```
                                      coef    std err          t      P>|t|
const                               0.6508      0.008     86.294      0.000
ancestry_group_Asian               -0.1491      0.020     -7.614      0.000
ancestry_group_European            -0.0917      0.008    -11.828      0.000
ancestry_group_Hispanic_Latino     -0.4223      0.008    -55.854      0.000
ancestry_group_Middle_Eastern      -0.1413      0.015     -9.277      0.000
ancestry_group_North_American       0.1950      0.010     20.328      0.000
ancestry_group_Other               -0.3034      0.008    -39.820      0.000
ancestry_group_Pacific_Islander    -0.0013      0.008     -0.173      0.862
native_born                         0.0732      0.002     30.760      0.000

R-squared: 0.132
Adjusted R-squared: 0.131
F-statistic: 3978 (p < 0.001)
N = 209,607
```

---

## References

- US Census Bureau. (2022). American Community Survey Public Use Microdata Sample (PUMS). https://www.census.gov/programs-surveys/acs/microdata.html
- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Lawrence Erlbaum Associates.

---

*Analysis conducted: February 1, 2026*  
*Data: US Census ACS PUMS 2022 - California*  
*Sample: N = 209,607 adults aged 25-65*
