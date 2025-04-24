import matplotlib.pyplot as plt
from statistics_generator import display_basic_summary, display_demographic_extremes
from visualization_data import (
    plot_top_countries, plot_growth_rates, plot_population_density,
    plot_urbanization, analyze_migration_patterns, analyze_fertility_vs_development,
    population_distribution_analysis
)

def display_menu():
    """Display the menu of available analyses."""
    print("\nWorld Population Analysis Menu:")
    print("1. Basic Summary Statistics")
    print("2. Top Countries by Population")
    print("3. Population Growth Rates")
    print("4. Population Density Analysis")
    print("5. Urbanization Analysis")
    print("6. Migration Patterns")
    print("7. Fertility vs Development")
    print("8. Population Distribution by Land Area")
    print("9. Demographic Extremes")
    print("0. Exit")
    return input("\nEnter your choice (0-9): ")

def run_menu_system(df_clean):
    """Run the interactive menu system."""
    while True:
        choice = display_menu()
        
        if choice == '0':
            print("Thank you for using the World Population Analysis tool!")
            break
            
        elif choice == '1':
            display_basic_summary(df_clean)
            
        elif choice == '2':
            n = int(input("Enter the number of top countries to display (default 15): ") or 15)
            plot_top_countries(df_clean, n)
            
        elif choice == '3':
            n = int(input("Enter the number of countries to display (default 15): ") or 15)
            plot_growth_rates(df_clean, n)
            
        elif choice == '4':
            n = int(input("Enter the number of countries to display (default 15): ") or 15)
            plot_population_density(df_clean, n)
            
        elif choice == '5':
            n = int(input("Enter the number of countries to display (default 15): ") or 15)
            plot_urbanization(df_clean, n)
            
        elif choice == '6':
            analyze_migration_patterns(df_clean)
            
        elif choice == '7':
            analyze_fertility_vs_development(df_clean)
            
        elif choice == '8':
            population_distribution_analysis(df_clean)
            
        elif choice == '9':
            display_demographic_extremes(df_clean)
            
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")
        plt.close('all')  # Close all open plots
        