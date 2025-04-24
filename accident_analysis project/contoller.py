from data_loading import load_data
from data_processing import clean_data, prepare_numeric_data
from data_analysis import basic_exploration, survival_analysis, speed_impact_analysis, correlation_analysis
from data_visualization import (plot_survival_by_factors, plot_speed_impact, 
                          plot_survival_by_speed_range, plot_correlation_matrix,
                          plot_relationship_scatter)
from user_interface import show_menu

def print_basic_exploration(results):
    """Print the results of basic data exploration"""
    print("Basic Data Exploration")
    print("-" * 30)
    
    print(f"Total number of records: {results['total_records']}")
    
    print("\nColumns present in the dataset:")
    for col in results['columns']:
        print(f"- {col}")
    
    print("\nMissing value detection:")
    for col, info in results['missing_values'].items():
        print(f"- {col}: {info['count']} missing values ({info['percentage']:.2f}%)")
    
    print(f"\nOverall survival rate: {results['overall_survival_rate']:.2f}%")

def print_survival_analysis(results):
    """Print the results of survival analysis"""
    print("\nSurvival Rate Analysis")
    print("-" * 30)
    
    print("\nSurvival rates by different factors:")
    
    print("\nGender:")
    print(results['gender_survival'])
    
    print("\nHelmet Usage:")
    print(results['helmet_survival'])
    
    print("\nSeatbelt Usage:")
    print(results['seatbelt_survival'])

def print_speed_analysis(results):
    """Print the results of speed impact analysis"""
    print("\nSpeed of Impact Analysis")
    print("-" * 30)
    
    print("\nDescriptive statistics for speed of impact:")
    print(results['speed_stats'])
    
    print("\nUnderstanding how impact speed correlates with survival:")
    print(results['speed_range_survival'])

def print_correlation_analysis(correlations):
    """Print the results of correlation analysis"""
    print("\nCorrelation Analysis")
    print("-" * 30)
    
    print("\nExamine relationships between Age, Speed of Impact, and Survival:")
    print(correlations.loc[['Age', 'Speed_of_Impact', 'Survived'], 
                         ['Age', 'Speed_of_Impact', 'Survived']])

def run_analysis():
    """Run the complete analysis process"""
    # Load the data
    data = load_data()
    
    # Process data
    clean_dataset = clean_data(data)
    numeric_dataset = prepare_numeric_data(data)
    
    # Run analyses
    basic_results = basic_exploration(data)
    survival_results = survival_analysis(data)
    speed_results = speed_impact_analysis(clean_dataset)
    correlation_results = correlation_analysis(numeric_dataset)
    
    # Print results
    print_basic_exploration(basic_results)
    print_survival_analysis(survival_results)
    print_speed_analysis(speed_results)
    print_correlation_analysis(correlation_results)
    
    # Get graph choice from user
    graph_choice = show_menu()
    
    # Show visualizations based on user choice
    try:
        if graph_choice in ["1", "6"]:
            plot_survival_by_factors(
                survival_results['gender_survival'],
                survival_results['helmet_survival'],
                survival_results['seatbelt_survival']
            )
        
        if graph_choice in ["2", "6"]:
            plot_speed_impact(clean_dataset)
        
        if graph_choice in ["3", "6"]:
            plot_survival_by_speed_range(speed_results['speed_range_survival'])
        
        if graph_choice in ["4", "6"]:
            plot_correlation_matrix(correlation_results)
        
        if graph_choice in ["5", "6"]:
            plot_relationship_scatter(numeric_dataset)
            
    except Exception as e:
        print(f"Error displaying graphs: {e}")
        print("Continuing without visualization.")
 