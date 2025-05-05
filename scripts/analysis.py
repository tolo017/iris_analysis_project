import pandas as pd

def basic_statistics(df):
    """Return basic statistics for numerical columns
    
    Args:
        df (DataFrame): Input dataframe with numerical columns
        
    Returns:
        DataFrame: Summary statistics
    """
    return df.describe()

def group_analysis(df, group_col='species'):
    """Return mean values grouped by specified column
    
    Args:
        df (DataFrame): Input dataframe
        group_col (str): Column to group by (default 'species')
        
    Returns:
        DataFrame: Grouped mean values
    """
    return df.groupby(group_col).mean()

def correlation_analysis(df):
    """Calculate correlation matrix for numerical features
    
    Args:
        df (DataFrame): Input dataframe
        
    Returns:
        DataFrame: Correlation matrix
    """
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    return df[numerical_cols].corr()