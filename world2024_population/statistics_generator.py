def generate_summary(df):
    """Generate summary statistics from the population data."""
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

def display_basic_summary(df_clean):
    """Display basic summary statistics."""
    summary = generate_summary(df_clean)
    print("\nWorld Population Summary:")
    print(f"Total World Population: {summary['total_world_population']:,.0f}")
    print(f"Top 10 Countries Population: {summary['top_10_population']:,.0f} ({summary['top_10_percent']:.1f}%)")
    print(f"Growing Countries: {summary['growing_countries_count']}")
    print(f"Shrinking Countries: {summary['shrinking_countries_count']}")
    print(f"Countries with High Population Density: {summary['high_density_countries']}")
    print(f"Countries with Net Immigration: {summary['immigration_countries']}")
    print(f"Countries with Net Emigration: {summary['emigration_countries']}")

def display_demographic_extremes(df_clean):
    """Display demographic extremes analysis."""
    highest_fertility = df_clean.sort_values('Fert. Rate', ascending=False).head(5)
    lowest_fertility = df_clean.sort_values('Fert. Rate').head(5)
    oldest_countries = df_clean.sort_values('Med. Age', ascending=False).head(5)
    youngest_countries = df_clean.sort_values('Med. Age').head(5)
    
    print("\nDemographic Extremes:")
    print(f"Highest Fertility Rates: {', '.join(highest_fertility['Country'] + ' (' + highest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Lowest Fertility Rates: {', '.join(lowest_fertility['Country'] + ' (' + lowest_fertility['Fert. Rate'].astype(str) + ')')}")
    print(f"Oldest Countries (Median Age): {', '.join(oldest_countries['Country'] + ' (' + oldest_countries['Med. Age'].astype(str) + ')')}")
    print(f"Youngest Countries (Median Age): {', '.join(youngest_countries['Country'] + ' (' + youngest_countries['Med. Age'].astype(str) + ')')}")
    