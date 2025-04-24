def show_menu():
    """Display the menu for graph selection"""
    print("\n" + "=" * 50)
    print("Analysis complete. Now you can choose which graphs to view.")
    print("Available graphs:")
    print("1. Survival rates by factors (gender, helmet, seatbelt)")
    print("2. Speed impact analysis (boxplot and histogram)")
    print("3. Survival rate by speed range")
    print("4. Correlation matrix heatmap")
    print("5. Relationship scatter plots")
    print("6. All graphs")
    print("0. No graphs")
    
    try:
        return input("\nEnter the number of the graph you want to see (0-6): ")
    except Exception:
        print("Error getting input. Defaulting to no graphs.")
        return "0"
    