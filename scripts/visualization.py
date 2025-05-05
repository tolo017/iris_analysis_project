import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def setup_visuals():
    """Set up consistent visualization style"""
    sns.set(style="whitegrid")
    plt.rcParams['figure.figsize'] = (8, 5)
    plt.rcParams['font.size'] = 12

def plot_species_comparison(df, feature, output_path=None):
    """Create bar plot comparing feature across species"""
    setup_visuals()
    plt.figure()
    ax = sns.barplot(x='species', y=feature, data=df)
    plt.title(f'Comparison of {feature} by Species')
    plt.ylabel(feature)
    
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def plot_distribution(df, feature, output_path=None):
    """Create histogram of a feature"""
    setup_visuals()
    plt.figure()
    sns.histplot(data=df, x=feature, hue='species', kde=True, element='step')
    plt.title(f'Distribution of {feature} by Species')
    
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def plot_scatter(df, x_feature, y_feature, output_path=None):
    """Create scatter plot of two features"""
    setup_visuals()
    plt.figure()
    sns.scatterplot(data=df, x=x_feature, y=y_feature, hue='species')
    plt.title(f'{x_feature} vs {y_feature} by Species')
    
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, bbox_inches='tight')
    plt.close()