import matplotlib.pyplot as plt
import seaborn as sns

def plot_survival_by_factors(gender_survival, helmet_survival, seatbelt_survival, save=True):
    """Plot survival rates by different factors"""
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
    if save:
        plt.savefig('survival_rates_by_factors.png')
    plt.show()

def plot_speed_impact(clean_data, save=True):
    """Plot the relationship between speed of impact and survival"""
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
    if save:
        plt.savefig('speed_impact_analysis.png')
    plt.show()

def plot_survival_by_speed_range(speed_range_survival, save=True):
    """Plot survival rate by speed range"""
    plt.figure(figsize=(8, 5))
    sns.barplot(x=speed_range_survival.index, y=speed_range_survival.values)
    plt.title('Survival Rate by Speed Range')
    plt.xlabel('Speed Range')
    plt.ylabel('Survival Rate (%)')
    plt.ylim(0, 100)
    if save:
        plt.savefig('survival_by_speed_range.png')
    plt.show()

def plot_correlation_matrix(correlations, save=True):
    """Plot correlation matrix heatmap"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    if save:
        plt.savefig('correlation_matrix.png')
    plt.show()

def plot_relationship_scatter(numeric_data, save=True):
    """Plot scatter plots showing relationships between variables"""
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
    if save:
        plt.savefig('relationship_scatter_plots.png')
    plt.show()
    