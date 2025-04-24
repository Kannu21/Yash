import pandas as pd

# Create DataFrame from the structured data
data = {
    'Name': ['Amit', 'Ankit', 'Kapil', 'Sulabh'],
    'Age': [28, 22, 32, 20],
    'City': ['Indore', 'Pune', 'Varanasi', 'Mau']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Add a new column 'Country' with the given values
df['Country'] = ['INDIA', 'JAPAN', 'INDIA', 'AUSTRALIA']

# Print the DataFrame with the new column
print("\nDataFrame with 'Country' column added:")
print(df)
