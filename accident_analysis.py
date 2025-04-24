import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("accident.csv")

# Basic Data Exploration
print("Basic Data Exploration")
print("-" * 40)

# Total number of records
total_records = len(df)
print(f"Total number of records: {total_records}")

# Columns present in the dataset
columns = df.columns.tolist()
print(f"Columns present in the dataset: {columns}")

# Missing value detection
missing_values = df.isnull().sum()
print("\nMissing value detection:")
print(missing_values)

# Overall survival rate
survival_rate = df['Survived'].mean() * 100
print(f"\nOverall survival rate: {survival_rate:.2f}%")

# Survival Rate Analysis
print("\nSurvival Rate Analysis")
print("-" * 40)

# By Gender
gender_survival = df.groupby('Gender', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Gender:")
print(gender_survival)

# By Helmet Usage
helmet_survival = df.groupby('Helmet_Used', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Helmet Usage:")
print(helmet_survival)

# By Seatbelt Usage
seatbelt_survival = df.groupby('Seatbelt_Used', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Seatbelt Usage:")
print(seatbelt_survival)

# Additional analysis: Speed impact on survival
print("\nAnalyzing Speed Impact on Survival")
print("-" * 40)

# Create a proper copy of the filtered DataFrame
df_speed = df.dropna(subset=['Speed_of_Impact']).copy()

# Create speed categories
speed_bins = [0, 30, 60, 90, 120]
speed_labels = ['Very Low (0-30)', 'Low (31-60)', 'High (61-90)', 'Very High (91-120)']
df_speed.loc[:, 'Speed_Category'] = pd.cut(df_speed['Speed_of_Impact'], bins=speed_bins, labels=speed_labels)

# Calculate survival rates by speed category
speed_survival = df_speed.groupby('Speed_Category', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Speed Category:")
print(speed_survival)

# Combined safety measures analysis
print("\nAnalyzing Combined Safety Measures")
print("-" * 40)

df = df.copy()  
df.loc[:, 'Safety_Measures'] = df.apply(
    lambda row: 'Both' if row['Helmet_Used'] == 'Yes' and row['Seatbelt_Used'] == 'Yes' 
                else ('Helmet Only' if row['Helmet_Used'] == 'Yes' and row['Seatbelt_Used'] == 'No'
                     else ('Seatbelt Only' if row['Helmet_Used'] == 'No' and row['Seatbelt_Used'] == 'Yes'
                          else 'None')), axis=1)

# Calculate survival rates by combined safety measures
safety_survival = df.groupby('Safety_Measures', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Combined Safety Measures:")
print(safety_survival)

# Age group analysis
print("\nAnalyzing Age Groups")
print("-" * 40)

age_bins = [0, 25, 40, 55, 70]
age_labels = ['Young (18-25)', 'Adult (26-40)', 'Middle-aged (41-55)', 'Senior (56-70)']

# Create age groups using .loc to avoid warning
df.loc[:, 'Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Calculate survival rates by age group
age_survival = df.groupby('Age_Group', observed=False)['Survived'].mean() * 100
print("\nSurvival rates by Age Group:")
print(age_survival)

print("\nAnalysis complete.")
