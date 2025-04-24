import pandas as pd

# Create the DataFrame with product data
data = {
    'Product': ['Laptop', 'Tablet', 'Smartphone'],
    'Price': [1000, 500, 700],
    'Quantity': [5, 10, 7]
}

# Create the DataFrame
product_df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(product_df)
print("\n")

# Calculate total sales using itertuples()
total_sales = 0
for row in product_df.itertuples():
    # Calculate sales for each product by multiplying price and quantity
    product_sales = row.Price * row.Quantity
    total_sales += product_sales
    
    # Optional: print each product's sales for clarity
    print(f"{row.Product}: {row.Price} × {row.Quantity} = {product_sales}")

# Print the total sales
print("\nAssignment 2 Output:")
print(f"Total sales: {total_sales}")