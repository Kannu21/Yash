import pandas as pd

# Create first DataFrame
data1 = {
    'Name': ['Amit', 'Ankit', 'Sulabh'],
    'Age': [25, 30, 22]
}
df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'Name': ['Amit', 'Ankit', 'Sulabh'],
    'City': ['Indore', 'Ghazipur', 'Mau']
}
df2 = pd.DataFrame(data2)

# Print both DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Join the two DataFrames on the 'Name' column
joined_df = pd.merge(df1, df2, on='Name')
print("\nJoined DataFrame:")
print(joined_df)

# Create a DataFrame from a CSV file
# Note: This assumes a file named 'employees.csv' exists in the current directory
# If you want to test this code, you can create a sample CSV file or comment out this section

try:
    # For demonstration purposes, let's create a sample employees.csv in memory
    sample_csv = """Name,Department,Salary
John,HR,50000
Jane,IT,60000
Mike,Finance,55000
Sara,Marketing,52000
"""
    
    with open('employees.csv', 'w') as f:
        f.write(sample_csv)
    
    # Read the CSV file
    employees_df = pd.read_csv('employees.csv')
    print("\nDataFrame from CSV file:")
    print(employees_df)
    
except Exception as e:
    print(f"\nNote: Could not read 'employees.csv'. Error: {e}")
    print("If you want to test CSV reading, please create a CSV file named 'employees.csv'")
    print("For demonstration, here's how you would read a CSV file:")
    print("employees_df = pd.read_csv('employees.csv')")
    