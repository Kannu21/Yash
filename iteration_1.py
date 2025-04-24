import pandas as pd

# 1: Iterating over pandas DataFrames
data = {
    'Name': ["Ankit", "Amit", "Ajay", "Ayush"],
    'Age': [24, 27, 22, 32],
    'City': ["Indore", "Pune", "Varanasi", "Indore"]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")

# Iterate over the rows of the DataFrame to calculate the sum of the 'Age' column without using the built-in sum function
age_sum = 0
for index, row in df.iterrows():
    age_sum += row['Age']
print(f"Sum of 'Age' column: {age_sum}")
print("\n")

# Iterate over the rows and print the 'Name' and 'City' of people who are older than 25
print("People older than 25:")
for index, row in df.iterrows():
    if row['Age'] > 25:
        print(f"Name: {row['Name']}, City: {row['City']}")
print("\n")

# Iterate over the rows to create a new column 'Age Group' that categorizes people as 'Young' (<=25) and 'Adult' (>25)
df['Age Group'] = ''
for index, row in df.iterrows():
    if row['Age'] <= 25:
        df.at[index, 'Age Group'] = 'Young'
    else:
        df.at[index, 'Age Group'] = 'Adult'
print("DataFrame with Age Group column:")
print(df)
print("\n")

# Iterate over each column and print the column name and the first value of each column
print("Column names and their first values:")
for column in df.columns:
    print(f"Column: {column}, First Value: {df[column].iloc[0]}")
print("\n")

# Iterate over the rows and create a new DataFrame that contains only those rows where the 'City' starts with the letter 'I'
cities_with_i = []
for index, row in df.iterrows():
    if row['City'].startswith('I'):
        cities_with_i.append(row)
df_cities_with_i = pd.DataFrame(cities_with_i)
print("DataFrame with cities starting with 'I':")
print(df_cities_with_i)