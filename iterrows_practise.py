import pandas as pd

# Create the DataFrame with sales data
data = {
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'Product': ['Laptop', 'Tablet', 'Smartphone'],
    'Sales_Amount': [5000, 3000, 7000],
    'Region': ['North', 'South', 'East']
}

# Create the DataFrame
sales_df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(sales_df)
print("\n")

# Iterate through the rows using iterrows() and print the message for each row
print("Assignment 1 Output:")
for index, row in sales_df.iterrows():
    print(f"On {row['Date']}, {row['Product']} had a sales of {row['Sales_Amount']} in the {row['Region']} region.")