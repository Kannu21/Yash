import pandas as pd

# 1. Create a DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Access the 'Age' of Bob using label-based indexing
bob_age = df.loc[df['Name'] == 'Bob', 'Age'].values[0]
print("Age of Bob using label-based indexing:")
print(bob_age)
print("\n")

# Access the 'City' of Charlie using position-based indexing
# First, find the index position of Charlie
charlie_index = df[df['Name'] == 'Charlie'].index[0]
charlie_city = df.iloc[charlie_index, 2]  # 2 is the position index for 'City' column
print("City of Charlie using position-based indexing:")
print(charlie_city)
print("\n")

# Select all rows where the 'Age' is greater than 30 using boolean indexing
older_than_30 = df[df['Age'] > 30]
print("Rows where Age is greater than 30 (boolean indexing):")
print(older_than_30)