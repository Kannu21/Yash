import pandas as pd

# 4. Create a DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
    'Occupation': ['Data Analyst', 'Software Dev', 'Data Scientist', 'Manager']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Slice the rows from index '1' to '2' (inclusive) and select the 'Name' and 'City' columns using label-based slicing
# This will select rows with index 1 and 2 (Bob and Charlie) and the Name and City columns
rows_1_to_2_name_city = df.loc[1:2, ['Name', 'City']]
print("Rows from index '1' to '2' (inclusive) with 'Name' and 'City' columns using label-based slicing:")
print(rows_1_to_2_name_city)
print("\n")

# Slice the rows from position 0 to 2 (exclusive) and select the first 2 columns (Name and Age) using position-based slicing
# This will select rows 0 and 1 (Alice and Bob) and columns 0 and 1 (Name and Age)
rows_0_to_2_first_2_columns = df.iloc[0:2, 0:2]
print("Rows from position 0 to 2 (exclusive) with first 2 columns (Name and Age) using position-based slicing:")
print(rows_0_to_2_first_2_columns)