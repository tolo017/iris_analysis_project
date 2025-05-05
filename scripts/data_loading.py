import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from pathlib import Path

def load_iris_data():
    """Load and prepare the iris dataset from sklearn"""
    iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                         columns=iris['feature_names'] + ['target'])
    iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    return iris_df

def save_to_csv(df, path='data/iris.csv'):
    """Save dataframe to CSV, creating directory if needed"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def load_from_csv(path='data/iris.csv'):
    """Load dataframe from CSV"""
    return pd.read_csv(path)

if __name__ == "__main__":
    # When run directly, save the iris data to CSV
    df = load_iris_data()
    save_to_csv(df)
    print("Iris dataset saved to data/iris.csv")