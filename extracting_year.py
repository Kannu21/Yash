import pandas as pd

# Create the transaction data DataFrame
data = {
    'Transaction_ID': [1, 2, 3, 4],
    'Date': ['2025-01-01', '2025-02-15', '2025-03-20', '2025-04-10']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Transaction Data:")
print(df)
print("\n")

# Method 1: Using pandas vectorized operation (not iteration, but most efficient)
print("Method 1: Using pandas datetime functionality")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
print(df)
print("\n")

# Reset DataFrame to original state for other methods
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Method 2: Using iterrows
print("Method 2: Using iterrows")
for index, row in df.iterrows():
    year = row['Date'].year
    df.at[index, 'Year'] = year
print(df)
print("\n")

# Reset DataFrame to original state for other methods
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Method 3: Using itertuples
print("Method 3: Using itertuples")
for row in df.itertuples():
    index = row.Index
    year = pd.to_datetime(row.Date).year
    df.at[index, 'Year'] = year
print(df)
print("\n")

# Method 4: Using apply function 
print("Method 4: Using apply function")
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].apply(lambda x: x.year)
print(df)