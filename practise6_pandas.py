import pandas as pd
import numpy as np

# 1. Read the CSV file into a DataFrame
df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')

# 2. Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# 3. Display summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# 4. Extract year from dt column and add as new column
# Convert dt to datetime format first
df['dt'] = pd.to_datetime(df['dt'])
df['year'] = df['dt'].dt.year

# 5. Calculate the average temperature by year for the filtered data
yearly_avg_temp = df.groupby('year')['AverageTemperature'].mean().reset_index()
print("\nAverage temperature by year (first 5 rows):")
print(yearly_avg_temp.head())

# 6. Find all missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# 7. Fill missing temperature values with the mean temperature
mean_temp = df['AverageTemperature'].mean()
df['AverageTemperature'] = df['AverageTemperature'].fillna(mean_temp)

# 8. Find the country with the highest average temperature
country_avg_temp = df.groupby('Country')['AverageTemperature'].mean().reset_index()
highest_temp_country = country_avg_temp.loc[country_avg_temp['AverageTemperature'].idxmax()]
print("\nCountry with highest average temperature:")
print(f"{highest_temp_country['Country']} with {highest_temp_country['AverageTemperature']:.2f}°C")

# Optional: Visualization of average temperatures by country (top 10 hottest)
print("\nTop 10 countries with highest average temperatures:")
top_10_hottest = country_avg_temp.sort_values('AverageTemperature', ascending=False).head(10)
print(top_10_hottest)

# Optional: Time series analysis of global temperature trends
yearly_global_avg = df.groupby('year')['AverageTemperature'].mean().reset_index()
print("\nGlobal average temperature trend (first and last 5 years):")
print("First 5 years:")
print(yearly_global_avg.head())
print("Last 5 years:")
print(yearly_global_avg.tail())

# Optional: Check if the dataset has temperature uncertainty information
if 'AverageTemperatureUncertainty' in df.columns:
    # Calculate average uncertainty by country
    country_uncertainty = df.groupby('Country')['AverageTemperatureUncertainty'].mean().reset_index()
    print("\nCountries with highest temperature measurement uncertainty (top 5):")
    top_5_uncertain = country_uncertainty.sort_values('AverageTemperatureUncertainty', ascending=False).head(5)
    print(top_5_uncertain)
    