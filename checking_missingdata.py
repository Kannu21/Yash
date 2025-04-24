import pandas as pd
import numpy as np

# Create the data DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, np.nan]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Data with Missing Values:")
print(df)
print("\n")

# Method 1: Using pandas vectorized operation (not iteration, but most efficient)
print("Method 1: Using pandas isna() function")
df['Age_Flag'] = df['Age'].isna()
print(df)
print("\n")

# Reset DataFrame to original state for other methods
df = pd.DataFrame(data)

# Method 2: Using iterrows
print("Method 2: Using iterrows")
df['Age_Flag'] = False  # Initialize the column with default value
for index, row in df.iterrows():
    if pd.isna(row['Age']):
        df.at[index, 'Age_Flag'] = True
print(df)
print("\n")

# Reset DataFrame to original state for other methods
df = pd.DataFrame(data)

# Method 3: Using itertuples (more efficient than iterrows)
print("Method 3: Using itertuples")
df['Age_Flag'] = False  # Initialize the column with default value
for row in df.itertuples():
    if pd.isna(row.Age):
        df.at[row.Index, 'Age_Flag'] = True
print(df)
print("\n")

# Method 4: Using apply function (more Pythonic)
print("Method 4: Using apply function")
df = pd.DataFrame(data)
df['Age_Flag'] = df['Age'].apply(lambda x: pd.isna(x))
print(df)