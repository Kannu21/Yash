from data_loader import load_population_data, clean_data
from menu_system import run_menu_system

def analyze_world_population():
    """Main analysis function that loads data and runs the menu system."""
    # Load and clean data
    df = load_population_data()
    df_clean = clean_data(df)
    
    # Run the interactive menu system
    run_menu_system(df_clean)
    
    return df_clean

if __name__ == "__main__":
    # Execute the analysis
    df_analyzed = analyze_world_population()
    