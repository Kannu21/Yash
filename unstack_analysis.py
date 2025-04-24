import pandas as pd

# Create the stacked Series as shown in the example
data = {
    ('2021-01-01', 'North'): 100,
    ('2021-01-01', 'South'): 200,
    ('2021-01-02', 'North'): 150,
    ('2021-01-02', 'South'): 250
}

# Create the Series with MultiIndex properly labeled
index = pd.MultiIndex.from_tuples(data.keys(), names=['Date', 'Region'])
stacked_df = pd.Series(data.values(), index=index, name='Sales')

print("Original stacked data:")
print(stacked_df)

# Now unstack() will work because 'Region' is properly defined as an index level
wide_df = stacked_df.unstack(level='Region')

# Reset index to make 'Date' a regular column
wide_df = wide_df.reset_index()

print("\nReshaped data (after unstack):")
print(wide_df)