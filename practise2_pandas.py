import pandas as pd
import numpy as np

# Exercise 2: Create a DataFrame with missing values

# Given data
names = ['Amit', 'Ankit', 'Kapil', 'Sulabh', 'Khushi']
ages = [28, 24, np.nan, 32, 24]  # NaN for missing value
cities = ['Indore', 'Pune', np.nan, 'Mau', 'Varanasi']  # NaN for missing value

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'City': cities
})

# Print the DataFrame
print("Original DataFrame with missing values:")
print(df)

# Fill missing values in 'Age' with the mean age
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
print("\nDataFrame after filling missing ages with mean age:")
print(df)

# Drop rows where any value is missing
df_cleaned = df.dropna()
print("\nDataFrame after dropping rows with any missing value:")
print(df_cleaned)

# Exercise 3: Create a DataFrame from structured data
data = {
    'Name': ['Amit', 'Ankit'],
    'Age': [28, 22],
    'City': ['Indore', 'Pune']
}

df2 = pd.DataFrame(data)
print("\nDataFrame created from structured data:")
print(df2)
