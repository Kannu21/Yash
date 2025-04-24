import pandas as pd

# Create the DataFrame from the given data
data = {
    'City': ['A', 'B', 'C'],
    '2021': [100, 200, 300],
    '2022': [150, 250, 350]
}

# Create the DataFrame
df = pd.DataFrame(data)

print("Original data (wide format):")
print(df)

# Use melt() to reshape from wide to long format
# '2021' and '2022' will be melted into 'Year' and 'Sales' columns
melted_df = pd.melt(
    df,
    id_vars=['City'],      # Column(s) to keep as is
    value_vars=['2021', '2022'],  # Columns to melt
    var_name='Year',       # Name for the new column containing the former column names
    value_name='Sales'     # Name for the new column containing the values
)

print("\nReshaped data (long format):")
print(melted_df)
