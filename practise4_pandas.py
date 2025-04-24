import pandas as pd

# Create DataFrame from the structured data
data = {
    'Name': ['Amit', 'Ankit', 'Kapil', 'Sulabh'],
    'Age': [28, 22, 32, 20],
    'City': ['Indore', 'Pune', 'Varanasi', 'Mau'],
    'Country': ['INDIA', 'JAPAN', 'INDIA', 'AUSTRALIA']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Select rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nRows where Age > 25:")
print(filtered_df)

# Drop the 'City' column
df_no_city = df.drop('City', axis=1)
print("\nDataFrame after dropping 'City' column:")
print(df_no_city)

# Group the DataFrame by 'Country' and find the average age
grouped_df = df.groupby('Country')['Age'].mean()
print("\nAverage age by Country:")
print(grouped_df)
