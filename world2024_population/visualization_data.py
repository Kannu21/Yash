import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_countries(df, n=15):
    """Plot top N countries by population."""
    top_n = df.head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Population (2024)', y='Country', data=top_n.sort_values('Population (2024)', ascending=True))
    plt.title(f'Top {n} Countries by Population (2024)')
    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_growth_rates(df, n=15):
    """Plot countries with highest growth rates."""
    top_growth = df.sort_values('Yearly Change', ascending=False).head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Yearly Change', y='Country', data=top_growth)
    plt.title(f'{n} Countries with Highest Population Growth Rates')
    plt.xlabel('Annual Growth Rate')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_population_density(df, n=15):
    """Plot countries with highest population density."""
    top_density = df.sort_values('Density (P/Km²)', ascending=False).head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Density (P/Km²)', y='Country', data=top_density)
    plt.title(f'{n} Countries with Highest Population Density')
    plt.xlabel('Population Density (people per km²)')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_urbanization(df, n=15):
    """Plot countries with highest and lowest urbanization rates."""
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
    """Analyze and visualize migration patterns."""
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
    """Analyze relationship between fertility rate, median age, and urbanization."""
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
    """Analyze population distribution by regions and land area."""
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
    