import pandas as pd

# Create the transaction data DataFrame
data = {
    'Transaction_ID': [1, 2, 3, 4, 5],
    'Customer_Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Amount_Spent': [50, 100, 200, 300, 150],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Transaction Data:")
print(df)
print("\n")

print("Method 1: Using groupby")
customer_totals_groupby = df.groupby('Customer_Name')['Amount_Spent'].sum()
print(customer_totals_groupby)
print("\n")

# Method 2: Using iteration with iterrows
print("Method 2: Using iterrows")
customer_totals_iterrows = {}
for index, row in df.iterrows():
    customer = row['Customer_Name']
    amount = row['Amount_Spent']
    
    if customer in customer_totals_iterrows:
        customer_totals_iterrows[customer] += amount
    else:
        customer_totals_iterrows[customer] = amount

print("Total amount spent per customer:")
for customer, total in customer_totals_iterrows.items():
    print(f"{customer}: ${total}")
print("\n")

# Method 3: Using iteration with itertuples (more efficient than iterrows)
print("Method 3: Using itertuples")
customer_totals_itertuples = {}
for row in df.itertuples():
    customer = row.Customer_Name
    amount = row.Amount_Spent
    
    if customer in customer_totals_itertuples:
        customer_totals_itertuples[customer] += amount
    else:
        customer_totals_itertuples[customer] = amount

print("Total amount spent per customer:")
for customer, total in customer_totals_itertuples.items():
    print(f"{customer}: ${total}")