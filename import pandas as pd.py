import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load the data
def load_population_data():
    df = pd.read_csv('World_Population_Data.csv')
    return df

# Data cleaning and preparation
def clean_data(df):
    # Convert string numbers with commas to float
    for col in ['Population (2024)', 'Net Change', 'Land Area (Km²)', 'Migrants (net)']:
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
    
    # Calculate regional statistics (using continents would be better, but we'll group by major regions)
    
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

# Main analysis function
def analyze_world_population():
    # Load data
    df = load_population_data()
    
    # Clean data
    df_clean = clean_data(df)
    
    # Generate summary statistics
    summary = generate_summary(df_clean)
    print("World Population Summary:")
    print(f"Total World Population: {summary['total_world_population']:,.0f}")
    print(f"Top 10 Countries Population: {summary['top_10_population']:,.0f} ({summary['top_10_percent']:.1f}%)")
    print(f"Growing Countries: {summary['growing_countries_count']}")
    print(f"Shrinking Countries: {summary['shrinking_countries_count']}")
    
    # Demographic indicators analysis
    highest_fertility = df_clean.sort_values('Fert. Rate', ascending=False).head(5)
    lowest_fertility = df_clean.sort_values('Fert. Rate').head(5)
    oldest_countries = df_clean.sort_values('Med. Age', ascending=False).head(5)
    youngest_countries = df_clean.sort_values('Med. Age').head(5)
    
    print("\nDemographic Extremes:")
    print(f"Highest Fertility Rates: {', '.join(highest_fertility['Country'] + ' (' + highest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Lowest Fertility Rates: {', '.join(lowest_fertility['Country'] + ' (' + lowest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Oldest Countries (Median Age): {', '.join(oldest_countries['Country'] + ' (' + oldest_countries['Med. Age'].astype(str) + ')')}")
    print(f"Youngest Countries (Median Age): {', '.join(youngest_countries['Country'] + ' (' + youngest_countries['Med. Age'].astype(str) + ')')}")
    
    # Visualizations
    plot_top_countries(df_clean)
    plot_growth_rates(df_clean)
    plot_population_density(df_clean)
    plot_urbanization(df_clean)
    analyze_migration_patterns(df_clean)
    analyze_fertility_vs_development(df_clean)
    population_distribution_analysis(df_clean)
    
    # Additional analyses
    # Calculate continents (approximation - in a real analysis you'd have proper continent data)
    # This is just to demonstrate grouping capability
    
    # Perform correlation analysis
    correlation_matrix = df_clean[['Yearly Change', 'Density (P/Km²)', 'Fert. Rate', 'Med. Age', 'Urban Pop %']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Between Demographic Indicators')
    plt.tight_layout()
    plt.show()
    
    return df_clean

# Execute the analysis directly
df_analyzed = analyze_world_population()
print("Analysis complete!")