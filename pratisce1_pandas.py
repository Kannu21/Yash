import pandas as pd

# Create the DataFrame with the given data
names = ['Amit', 'Ankit', 'Kapil', 'Sulabh']
ages = [28, 24, 35, 32]
cities = ['Indore', 'Pune', 'Indore', 'Mau']

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'City': cities
})

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Display the first two rows
print("\nFirst two rows:")
print(df.head(2))

# Sort the DataFrame by age in descending order
df_sorted = df.sort_values(by='Age', ascending=False)
print("\nSorted by age (descending):")
print(df_sorted)

# Select the rows where age is greater than 30
df_filtered = df[df['Age'] > 30]
print("\nRows where age > 30:")
print(df_filtered)

# Select only the Name and City columns
df_selected = df[['Name', 'City']]
print("\nOnly Name and City columns:")
print(df_selected)

# Increase everyone's salary by 5%
# Note: Since we don't have a salary column in the initial data,
# let's add a salary column first for demonstration
df['Salary'] = [50000, 45000, 60000, 55000]  # Adding sample salaries
print("\nDataFrame with salary:")
print(df)

# Increase salary by 5%
df['Salary'] = df['Salary'] * 1.05
print("\nDataFrame with 5% increased salary:")
print(df)
