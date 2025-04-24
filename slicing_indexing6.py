import pandas as pd

# 6. Create a DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
    'Occupation': ['Data Analyst', 'Software Dev', 'Data Scientist', 'Manager']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame with default index:")
print(df)
print("\n")

# Set the 'Name' column as the index of the DataFrame using set_index() method
df_name_index = df.set_index('Name')
print("DataFrame with 'Name' as index:")
print(df_name_index)
print("\n")

# Reset the index back to the default integer index
df_reset = df_name_index.reset_index()
print("DataFrame with reset index:")
print(df_reset)