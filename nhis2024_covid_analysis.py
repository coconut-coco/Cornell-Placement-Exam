# ------------------------------
# 1. Load Libraries and Dataset
# ------------------------------
import pandas as pd
import numpy as np
df = pd.read_csv('/mnt/data/adult24.csv')
# ------------------------------
# 2. Data Preprocessing
#    - Rename key variables for readability
#    - Map coded values to labels
# ------------------------------
df = df.rename(columns={
    'SEX_A': 'Sex',
    'AGE_A': 'Age',
    'RACERPI_A': 'Race',
    'REGION_E': 'Region',
    'CVDEXP_A': 'HadCOVID',
    'CVDLONG_A': 'LongCOVID',
    'CVDLNGFAT_A': 'Fatigue',
    'CVDLNGHRB_A': 'Heart',
    'CVDLNGDIZ_A': 'Dizziness',
    'BMI_A': 'BMI',
    'SMKEV_A': 'Smoked',
    'WEIGHTLBTC_A': 'Weight'
})
# Recoding variables
df['Sex'] = df['Sex'].replace({1: 'Male', 2: 'Female'})
df['Race'] = df['Race'].replace({1: 'White', 2: 'Black', 3: 'Asian', 4: 'Other', 5: 'Other'})
df['Region'] = df['Region'].replace({1: 'Northeast', 2: 'Midwest', 3: 'South', 4: 'West'})
df['HadCOVID'] = df['HadCOVID'].replace({1: 'Yes', 2: 'No'})
df['LongCOVID'] = df['LongCOVID'].replace({1: 'Yes', 2: 'No'})
df['Fatigue'] = df['Fatigue'].replace({1: 'Yes', 2: 'No'})
df['Smoked'] = df['Smoked'].replace({1: 'Never', 2: 'Former', 3: 'Current'})
# ------------------------------
# 3. Descriptive Statistics (Table 1)
# ------------------------------
table1 = df.groupby('Sex').agg({'Age': 'mean', 'HadCOVID': lambda x: (x == 'Yes').mean() * 100, 'Sex': 'count'}).rename(columns={'Sex': 'Count'})
table1['Age'] = table1['Age'].round(1)
table1['HadCOVID'] = table1['HadCOVID'].round(1)
# Repeat for Race and Region
race_summary = df.groupby('Race').agg({'Age': 'mean', 'HadCOVID': lambda x: (x == 'Yes').mean() * 100, 'Race': 'count'}).rename(columns={'Race': 'Count'})
region_summary = df.groupby('Region').agg({'Age': 'mean', 'HadCOVID': lambda x: (x == 'Yes').mean() * 100, 'Region': 'count'}).rename(columns={'Region': 'Count'})
# ------------------------------
# 4. Symptom Analysis by Demographics
# ------------------------------
# Fatigue by Sex
fatigue_by_sex = df.groupby('Sex')['Fatigue'].value_counts(normalize=True).unstack().fillna(0) * 100
# Fatigue by Race
fatigue_by_race = df.groupby('Race')['Fatigue'].value_counts(normalize=True).unstack().fillna(0) * 100
# Fatigue by Region
fatigue_by_region = df.groupby('Region')['Fatigue'].value_counts(normalize=True).unstack().fillna(0) * 100
# Long COVID by Region
longcovid_by_region = df.groupby('Region')['LongCOVID'].value_counts(normalize=True).unstack().fillna(0) * 100
# ------------------------------
# 5. Relationship with Biological and Lifestyle Variables
# ------------------------------
# Categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5: return 'Underweight'
    elif bmi < 25: return 'Normal'
    elif bmi < 30: return 'Overweight'
    else: return 'Obese'
df['BMI_Category'] = df['BMI'].apply(categorize_bmi)
# Fatigue by BMI category
fatigue_by_bmi = df.groupby('BMI_Category')['Fatigue'].value_counts(normalize=True).unstack().fillna(0) * 100
# Fatigue by Smoking status
fatigue_by_smoke = df.groupby('Smoked')['Fatigue'].value_counts(normalize=True).unstack().fillna(0) * 100
# ------------------------------
# 6. Export to Word (optional step)
# ------------------------------
# You may use python-docx to generate a report from results (see previous code for implementation)