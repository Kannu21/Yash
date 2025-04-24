import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_accident_data():
    # Load the data
    data = pd.read_csv('accident.csv')
    
    # Basic Data Exploration
    print("Basic Data Exploration")
    print("-" * 30)
    
    # Total number of records
    print(f"Total number of records: {len(data)}")
    
    # Columns present in the dataset
    print("\nColumns present in the dataset:")
    for col in data.columns:
        print(f"- {col}")
    
    # Missing value detection
    print("\nMissing value detection:")
    for col in data.columns:
        missing = data[col].isna().sum()
        if missing > 0:
            print(f"- {col}: {missing} missing values ({missing/len(data)*100:.2f}%)")
    
    # Overall survival rate
    survival_rate = data['Survived'].mean() * 100
    print(f"\nOverall survival rate: {survival_rate:.2f}%")
    
    # Survival Rate Analysis
    print("\nSurvival Rate Analysis")
    print("-" * 30)
    
    # Survival rates by different factors
    print("\nSurvival rates by different factors:")
    
    # Gender
    print("\nGender:")
    gender_survival = data.groupby('Gender')['Survived'].mean() * 100
    print(gender_survival)
    
    # Helmet Usage
    print("\nHelmet Usage:")
    helmet_survival = data.groupby('Helmet_Used')['Survived'].mean() * 100
    print(helmet_survival)
    
    # Seatbelt Usage
    print("\nSeatbelt Usage:")
    seatbelt_survival = data.groupby('Seatbelt_Used')['Survived'].mean() * 100
    print(seatbelt_survival)
    
    # Speed of Impact Analysis
    print("\nSpeed of Impact Analysis")
    print("-" * 30)
    
    # Clean data by removing NaN values for speed
    clean_data = data.dropna(subset=['Speed_of_Impact']).copy()  # Create a proper copy
    
    # Descriptive statistics for speed of impact
    print("\nDescriptive statistics for speed of impact:")
    speed_stats = clean_data['Speed_of_Impact'].describe()
    print(speed_stats)
    
    # Understanding how impact speed correlates with survival
    print("\nUnderstanding how impact speed correlates with survival:")
    
    # Calculate survival rate at different speed ranges - fixing the warning
    clean_data.loc[:, 'Speed_Range'] = pd.cut(clean_data['Speed_of_Impact'], 
                                     bins=[0, 30, 60, 90, 120],
                                     labels=['0-30', '31-60', '61-90', '91-120'])
    
    # Fixed line with observed parameter explicitly set
    speed_range_survival = clean_data.groupby('Speed_Range', observed=False)['Survived'].mean() * 100
    print(speed_range_survival)
    
    # Correlation Analysis
    print("\nCorrelation Analysis")
    print("-" * 30)
    
    # Create a copy of the data with numeric values only
    numeric_data = data.copy()
    
    # Convert categorical variables to numeric
    numeric_data['Gender'] = numeric_data['Gender'].map({'Male': 0, 'Female': 1})
    numeric_data['Helmet_Used'] = numeric_data['Helmet_Used'].map({'No': 0, 'Yes': 1})
    numeric_data['Seatbelt_Used'] = numeric_data['Seatbelt_Used'].map({'No': 0, 'Yes': 1})
    
    # Drop rows with missing values for correlation analysis
    numeric_data = numeric_data.dropna()
    
    # Calculate correlations
    correlations = numeric_data[['Age', 'Speed_of_Impact', 'Survived', 
                               'Gender', 'Helmet_Used', 'Seatbelt_Used']].corr()
    
    print("\nExamine relationships between Age, Speed of Impact, and Survival:")
    print(correlations.loc[['Age', 'Speed_of_Impact', 'Survived'], 
                          ['Age', 'Speed_of_Impact', 'Survived']])
    
    # After completing all analysis, show graph options and ask user
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
        graph_choice = input("\nEnter the number of the graph you want to see (0-6): ")
        visualize_data(data, clean_data, numeric_data, gender_survival, 
                      helmet_survival, seatbelt_survival, speed_range_survival, 
                      correlations, graph_choice)
    except Exception as e:
        print(f"Error displaying graphs: {e}")
        print("Continuing without visualization.")

def visualize_data(data, clean_data, numeric_data, gender_survival, 
                  helmet_survival, seatbelt_survival, speed_range_survival, 
                  correlations, graph_choice):
    """Separate function to handle visualizations based on user choice"""
    
    if graph_choice == "0":
        print("No graphs selected. Exiting visualization.")
        return
    
    if graph_choice in ["1", "6"]:
        # Visualize survival rates by factors
        plt.figure(figsize=(15, 5))
        
        # Gender
        plt.subplot(1, 3, 1)
        sns.barplot(x=gender_survival.index, y=gender_survival.values)
        plt.title('Survival Rate by Gender')
        plt.ylabel('Survival Rate (%)')
        plt.ylim(0, 100)
        
        # Helmet Usage
        plt.subplot(1, 3, 2)
        sns.barplot(x=helmet_survival.index, y=helmet_survival.values)
        plt.title('Survival Rate by Helmet Usage')
        plt.ylabel('Survival Rate (%)')
        plt.ylim(0, 100)
        
        # Seatbelt Usage
        plt.subplot(1, 3, 3)
        sns.barplot(x=seatbelt_survival.index, y=seatbelt_survival.values)
        plt.title('Survival Rate by Seatbelt Usage')
        plt.ylabel('Survival Rate (%)')
        plt.ylim(0, 100)
        
        plt.tight_layout()
        plt.savefig('survival_rates_by_factors.png')
        plt.show()
    
    if graph_choice in ["2", "6"]:
        # Visualization of survival vs. speed of impact
        plt.figure(figsize=(10, 6))
        
        # Box plot
        plt.subplot(1, 2, 1)
        sns.boxplot(x='Survived', y='Speed_of_Impact', data=clean_data)
        plt.title('Speed of Impact vs Survival')
        plt.xlabel('Survived (0=No, 1=Yes)')
        plt.ylabel('Speed of Impact')
        
        # Histogram by survival
        plt.subplot(1, 2, 2)
        sns.histplot(data=clean_data, x='Speed_of_Impact', hue='Survived', element='step', common_norm=False, bins=10)
        plt.title('Distribution of Speed by Survival Status')
        plt.xlabel('Speed of Impact')
        plt.ylabel('Count')
        
        plt.tight_layout()
        plt.savefig('speed_impact_analysis.png')
        plt.show()
    
    if graph_choice in ["3", "6"]:
        # Visualize survival rate by speed range
        plt.figure(figsize=(8, 5))
        sns.barplot(x=speed_range_survival.index, y=speed_range_survival.values)
        plt.title('Survival Rate by Speed Range')
        plt.xlabel('Speed Range')
        plt.ylabel('Survival Rate (%)')
        plt.ylim(0, 100)
        plt.savefig('survival_by_speed_range.png')
        plt.show()
    
    if graph_choice in ["4", "6"]:
        # Visualize correlations
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png')
        plt.show()
    
    if graph_choice in ["5", "6"]:
        # Scatter plots for relationships
        plt.figure(figsize=(15, 5))
        
        # Age vs Survival
        plt.subplot(1, 3, 1)
        sns.scatterplot(x='Age', y='Survived', data=numeric_data, alpha=0.5)
        plt.title('Age vs Survival')
        
        # Speed of Impact vs Survival
        plt.subplot(1, 3, 2)
        sns.scatterplot(x='Speed_of_Impact', y='Survived', data=numeric_data, alpha=0.5)
        plt.title('Speed of Impact vs Survival')
        
        # Age vs Speed of Impact
        plt.subplot(1, 3, 3)
        sns.scatterplot(x='Age', y='Speed_of_Impact', data=numeric_data, alpha=0.5, hue='Survived')
        plt.title('Age vs Speed of Impact\n(colored by survival)')
        
        plt.tight_layout()
        plt.savefig('relationship_scatter_plots.png')
        plt.show()

# Run the analysis
analyze_accident_data()
