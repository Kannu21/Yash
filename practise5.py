import numpy as np

def create_sales_report():
    # Create sales data for 4 products across 3 regions over 6 months
    # Shape: (6 months, 3 regions, 4 products)
    sales = np.random.randint(1000, 5000, size=(6, 3, 4))
    
    # Create labels for better understanding
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    regions = ['North', 'East', 'South']
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    
    print("Sales Data Shape:", sales.shape)
    print("\nInitial Sales Data Structure:")
    print(sales)
    
    def analyze_sales():
        # 1. Total sales for January
        jan_sales = np.sum(sales[0])
        print(f"\n1. Total {months[0]} Sales: {jan_sales}")
        
        # 2. March sales for second product across regions
        march_prod2 = sales[2, :, 1]
        print(f"\n2. {months[2]} sales for {products[1]} by region:")
        for region, sale in zip(regions, march_prod2):
            print(f"   {region}: {sale}")
        
        # 3. April sales in Eastern region
        april_east = sales[3, 1, :]
        print(f"\n3. {months[3]} sales in {regions[1]} region:")
        for product, sale in zip(products, april_east):
            print(f"   {product}: {sale}")
        
        # 4. First quarter sales
        q1_sales = sales[:3]
        print("\n4. First Quarter Sales Summary:")
        for i, month in enumerate(months[:3]):
            print(f"\n   {month}:")
            for j, region in enumerate(regions):
                print(f"      {region}: {q1_sales[i,j]}")
    
    def calculate_statistics():
        print("\nSales Statistics:")
        
        # Monthly statistics
        monthly_totals = np.sum(sales, axis=(1,2))
        best_month_idx = np.argmax(monthly_totals)
        print(f"\nBest Month: {months[best_month_idx]}")
        print(f"Sales: {monthly_totals[best_month_idx]}")
        
        # Regional statistics
        regional_totals = np.sum(sales, axis=(0,2))
        best_region_idx = np.argmax(regional_totals)
        print(f"\nBest Region: {regions[best_region_idx]}")
        print(f"Sales: {regional_totals[best_region_idx]}")
        
        # Product statistics
        product_totals = np.sum(sales, axis=(0,1))
        best_product_idx = np.argmax(product_totals)
        print(f"\nBest Product: {products[best_product_idx]}")
        print(f"Sales: {product_totals[best_product_idx]}")
        
        # Average sales per month
        monthly_averages = np.mean(sales, axis=(1,2))
        print("\nMonthly Averages:")
        for month, avg in zip(months, monthly_averages):
            print(f"{month}: {avg:.2f}")
    
    # Run the analyses
    analyze_sales()
    calculate_statistics()

# Execute the report
create_sales_report()