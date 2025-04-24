import pandas as pd

# 2: Several iteration-based operations
# Sample DataFrame
data = {
    'Name': ["Ayush", "Ankit", "Amit", "Sulabh"],
    'Age': [24, 27, 22, 32],
    'City': ["Indore", "Ghazipur", "Indore", "Mau"]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")

# Write a function to iterate through each row and print index and values
def print_rows_with_index():
    print("Row indices and values:")
    for index, row in df.iterrows():
        print(f"Index: {index}, Values: {dict(row)}")

# Write a function to iterate through each row and print specific columns
def print_specific_columns():
    print("Name and City columns:")
    for index, row in df.iterrows():
        print(f"Name: {row['Name']}, City: {row['City']}")

# Write a function to count rows where 'Age' > 25
def count_age_greater_than_25():
    count = 0
    for index, row in df.iterrows():
        if row['Age'] > 25:
            count += 1
    return count

# Write a function to increment 'Age' by 2 years
def increment_age():
    for index, row in df.iterrows():
        df.at[index, 'Age'] = row['Age'] + 2
    return df

# Write a function to print max and min values of each column
def print_min_max_values():
    min_values = {}
    max_values = {}
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            min_values[column] = df[column].min()
            max_values[column] = df[column].max()
    print(f"Min values: {min_values}")
    print(f"Max values: {max_values}")

# Write a function to compute average 'Age' for each city
def average_age_by_city():
    city_age = {}
    for city in df['City'].unique():
        city_rows = df[df['City'] == city]
        city_age[city] = city_rows['Age'].mean()
    return city_age

# Write a function to find rows where 'City' is 'Indore' or 'Mau'
def find_specific_cities():
    specific_cities = []
    for index, row in df.iterrows():
        if row['City'] in ['Indore', 'Mau']:
            specific_cities.append(row)
    return pd.DataFrame(specific_cities)

# Write a function to display original DataFrame
def display_original_df():
    return df

# Execute all functions
print_rows_with_index()
print("\n")

print_specific_columns()
print("\n")

age_count = count_age_greater_than_25()
print(f"Count of people with age > 25: {age_count}")
print("\n")

print("DataFrame after incrementing age by 2:")
df_incremented = increment_age()
print(df_incremented)
print("\n")

print_min_max_values()
print("\n")

avg_age = average_age_by_city()
print("Average age by city:")
for city, avg in avg_age.items():
    print(f"City: {city}, Average Age: {avg:.2f}")
print("\n")

specific_cities_df = find_specific_cities()
print("Rows where City is 'Indore' or 'Mau':")
print(specific_cities_df)
print("\n")

print("Original DataFrame (note: ages have been incremented previously):")
print(display_original_df())