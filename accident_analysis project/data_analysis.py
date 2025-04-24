def basic_exploration(data):
    """Perform basic data exploration"""
    results = {}
    
    # Total number of records
    results['total_records'] = len(data)
    
    # Columns present in the dataset
    results['columns'] = list(data.columns)
    
    # Missing value detection
    missing_values = {}
    for col in data.columns:
        missing = data[col].isna().sum()
        if missing > 0:
            missing_values[col] = {
                'count': missing,
                'percentage': missing/len(data)*100
            }
    results['missing_values'] = missing_values
    
    # Overall survival rate
    results['overall_survival_rate'] = data['Survived'].mean() * 100
    
    return results

def survival_analysis(data):
    """Analyze survival rates by different factors"""
    results = {}
    
    # Gender
    results['gender_survival'] = data.groupby('Gender')['Survived'].mean() * 100
    
    # Helmet Usage
    results['helmet_survival'] = data.groupby('Helmet_Used')['Survived'].mean() * 100
    
    # Seatbelt Usage
    results['seatbelt_survival'] = data.groupby('Seatbelt_Used')['Survived'].mean() * 100
    
    return results

def speed_impact_analysis(clean_data):
    """Analyze the impact of speed on survival"""
    results = {}
    
    # Descriptive statistics for speed of impact
    results['speed_stats'] = clean_data['Speed_of_Impact'].describe()
    
    # Calculate survival rate at different speed ranges
    results['speed_range_survival'] = clean_data.groupby('Speed_Range', observed=False)['Survived'].mean() * 100
    
    return results

def correlation_analysis(numeric_data):
    """Perform correlation analysis on numeric data"""
    # Calculate correlations
    correlations = numeric_data[['Age', 'Speed_of_Impact', 'Survived', 
                               'Gender', 'Helmet_Used', 'Seatbelt_Used']].corr()
    
    return correlations
