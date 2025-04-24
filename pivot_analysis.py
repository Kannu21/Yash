import pandas as pd

# Create the DataFrame from the given data
data = {
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [100, 200, 150, 250]
}

df = pd.DataFrame(data)

# Use pivot() to reshape the data with regions as columns
pivot_df = df.pivot_table(
    index=['Date', 'Product'],
    columns='Region',
    values='Sales',
    aggfunc='sum'
)

# Reset index to make Date and Product regular columns
pivot_df = pivot_df.reset_index()

print("Original Data:")
print(df)
print("\nReshaped Data (pivot):")
print(pivot_df)
