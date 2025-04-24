import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

# Load the data
def load_population_data():
    df = pd.read_csv('test.csv')
    return df

# Data cleaning and preparation
def clean_data(df):
    # Convert string numbers with commas to float
    for col in ['Population (2024)', 'Net Change', 'Land Area (Km²)', 'Migrants (net)', 'Density (P/Km²)']:
        df[col] = df[col].str.replace(',', '').astype(float)
    
    # Convert percentages to float
    for col in ['Yearly Change', 'World Share']:
        df[col] = df[col].str.rstrip(' %').astype(float) / 100
    
    # Handle special cases like "N.A." in Urban Pop %
    df['Urban Pop %'] = df['Urban Pop %'].replace('N.A.', np.nan)
    df['Urban Pop %'] = df['Urban Pop %'].str.rstrip(' %').astype(float) / 100
    
    return df

# Basic statistics and summary
def generate_summary(df):
    # Total world population
    total_population = df['Population (2024)'].sum()
    
    # Calculate regional statistics
    top_10 = df.head(10)
    rest_of_world = df.iloc[10:]
    
    # Growth metrics
    growing_countries = df[df['Yearly Change'] > 0]
    shrinking_countries = df[df['Yearly Change'] < 0]
    
    # Density analysis
    high_density = df[df['Density (P/Km²)'] > 1000]
    
    # Migration patterns
    immigration_countries = df[df['Migrants (net)'] > 0]
    emigration_countries = df[df['Migrants (net)'] < 0]
    
    summary = {
        'total_world_population': total_population,
        'top_10_population': top_10['Population (2024)'].sum(),
        'top_10_percent': top_10['Population (2024)'].sum() / total_population * 100,
        'growing_countries_count': len(growing_countries),
        'shrinking_countries_count': len(shrinking_countries),
        'high_density_countries': len(high_density),
        'immigration_countries': len(immigration_countries),
        'emigration_countries': len(emigration_countries)
    }
    
    return summary

# Visualization functions
def plot_top_countries(df, n=15):
    """Plot top N countries by population"""
    top_n = df.head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Population (2024)', y='Country', data=top_n.sort_values('Population (2024)', ascending=True))
    plt.title(f'Top {n} Countries by Population (2024)')
    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_growth_rates(df, n=15):
    """Plot countries with highest growth rates"""
    top_growth = df.sort_values('Yearly Change', ascending=False).head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Yearly Change', y='Country', data=top_growth)
    plt.title(f'{n} Countries with Highest Population Growth Rates')
    plt.xlabel('Annual Growth Rate')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_population_density(df, n=15):
    """Plot countries with highest population density"""
    top_density = df.sort_values('Density (P/Km²)', ascending=False).head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Density (P/Km²)', y='Country', data=top_density)
    plt.title(f'{n} Countries with Highest Population Density')
    plt.xlabel('Population Density (people per km²)')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_urbanization(df, n=15):
    """Plot countries with highest and lowest urbanization rates"""
    # Drop NA values
    df_urban = df.dropna(subset=['Urban Pop %'])
    
    # Top urbanized
    top_urban = df_urban.sort_values('Urban Pop %', ascending=False).head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Urban Pop %', y='Country', data=top_urban)
    plt.title(f'{n} Most Urbanized Countries')
    plt.xlabel('Urban Population Percentage')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()
    
    # Least urbanized
    bottom_urban = df_urban.sort_values('Urban Pop %').head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Urban Pop %', y='Country', data=bottom_urban)
    plt.title(f'{n} Least Urbanized Countries')
    plt.xlabel('Urban Population Percentage')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def analyze_migration_patterns(df):
    """Analyze and visualize migration patterns"""
    # Top immigration countries
    top_immigration = df.sort_values('Migrants (net)', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Migrants (net)', y='Country', data=top_immigration)
    plt.title('Top 10 Countries by Net Immigration')
    plt.xlabel('Net Migration')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()
    
    # Top emigration countries
    top_emigration = df.sort_values('Migrants (net)').head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Migrants (net)', y='Country', data=top_emigration)
    plt.title('Top 10 Countries by Net Emigration')
    plt.xlabel('Net Migration')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def analyze_fertility_vs_development(df):
    """Analyze relationship between fertility rate, median age, and urbanization"""
    plt.figure(figsize=(12, 8))
    
    # Drop NA values
    df_clean = df.dropna(subset=['Urban Pop %', 'Fert. Rate', 'Med. Age'])
    
    # Create scatter plot with color representing urbanization
    plt.scatter(df_clean['Med. Age'], df_clean['Fert. Rate'], 
                c=df_clean['Urban Pop %'], cmap='viridis', 
                s=df_clean['Population (2024)'] / 10**7, alpha=0.7)
    
    plt.colorbar(label='Urbanization Rate')
    plt.xlabel('Median Age')
    plt.ylabel('Fertility Rate')
    plt.title('Relationship Between Median Age, Fertility Rate, and Urbanization')
    
    # Annotate some notable countries
    for idx, row in df_clean.head(10).iterrows():
        plt.annotate(row['Country'], (row['Med. Age'], row['Fert. Rate']))
    
    plt.tight_layout()
    plt.show()

def population_distribution_analysis(df):
    """Analyze population distribution by regions and land area"""
    # Calculate population to land area ratio
    df['Pop_Land_Ratio'] = df['Population (2024)'] / df['Land Area (Km²)']
    
    # Plot the distribution of population by land area
    plt.figure(figsize=(10, 8))
    plt.scatter(df['Land Area (Km²)'], df['Population (2024)'], 
                alpha=0.7, c=df['Density (P/Km²)'], cmap='plasma', norm=plt.Normalize(0, 1000))
    plt.colorbar(label='Population Density')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Land Area (km²) - Log Scale')
    plt.ylabel('Population - Log Scale')
    plt.title('Population vs Land Area (2024)')
    
    # Annotate some notable countries
    for idx, row in df.iloc[list(range(5)) + [10, 20, 30]].iterrows():
        plt.annotate(row['Country'], (row['Land Area (Km²)'], row['Population (2024)']))
    
    plt.tight_layout()
    plt.show()

def display_menu():
    """Display the menu of available analyses"""
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

def display_demographic_extremes(df_clean):
    """Display demographic extremes analysis"""
    highest_fertility = df_clean.sort_values('Fert. Rate', ascending=False).head(5)
    lowest_fertility = df_clean.sort_values('Fert. Rate').head(5)
    oldest_countries = df_clean.sort_values('Med. Age', ascending=False).head(5)
    youngest_countries = df_clean.sort_values('Med. Age').head(5)
    
    print("\nDemographic Extremes:")
    print(f"Highest Fertility Rates: {', '.join(highest_fertility['Country'] + ' (' + highest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Lowest Fertility Rates: {', '.join(lowest_fertility['Country'] + ' (' + lowest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Oldest Countries (Median Age): {', '.join(oldest_countries['Country'] + ' (' + oldest_countries['Med. Age'].astype(str) + ')')}")
    print(f"Youngest Countries (Median Age): {', '.join(youngest_countries['Country'] + ' (' + youngest_countries['Med. Age'].astype(str) + ')')}")

def display_basic_summary(df_clean):
    """Display basic summary statistics"""
    summary = generate_summary(df_clean)
    print("\nWorld Population Summary:")
    print(f"Total World Population: {summary['total_world_population']:,.0f}")
    print(f"Top 10 Countries Population: {summary['top_10_population']:,.0f} ({summary['top_10_percent']:.1f}%)")
    print(f"Growing Countries: {summary['growing_countries_count']}")
    print(f"Shrinking Countries: {summary['shrinking_countries_count']}")
    print(f"Countries with High Population Density: {summary['high_density_countries']}")
    print(f"Countries with Net Immigration: {summary['immigration_countries']}")
    print(f"Countries with Net Emigration: {summary['emigration_countries']}")

def analyze_world_population():
    """Main analysis function with interactive menu"""
    # Load and clean data
    df = load_population_data()
    df_clean = clean_data(df)
    
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
    
    return df_clean

# Execute the analysis
df_analyzed = analyze_world_population()
