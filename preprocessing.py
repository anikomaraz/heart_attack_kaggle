################# IMPORTS #################

import numpy as np
import pandas as pd

from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    OneHotEncoder,
)

from sklearn.metrics import accuracy_score, classification_report

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

# Import custom functions for feature splitting
from utils import split_blood_pressure, split_cholesterol_sample


################# DATA TRANSFORMATIONS #################

def load_data(file_path):
    """
    Loads data from CSV file.

    Returns a pandas.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)


def create_new_features(df):
    """
    Applies custom feature splitting functions to create new features.

    Returns a pandas.DataFrame with new features added.
    """
    df_copy = df.copy()
    split_blood_pressure(df_copy)
    split_cholesterol_sample(df_copy)
    return df_copy


def select_features(df, continuous_vars, categorical_vars):
    """
    Selects specified features from the DataFrame.

    Parameters:
    df (pandas.DataFrame): Input DataFrame.
    continuous_vars (list): List of continuous variable names.
    categorical_vars (list): List of categorical variable names.

    Returns:
    pandas.DataFrame: DataFrame containing selected features.
    """
    return df[continuous_vars + categorical_vars]


def preprocess_data(X, num_transformer, cat_transformer):
    """
    Applies preprocessing steps to the data using ColumnTransformer.

    Returns a numpy.ndarray: Transformed data array.
    """
    preproc_basic = ColumnTransformer(
        transformers=[
            ("num", num_transformer, continuous_vars),
            ("cat", cat_transformer, categorical_vars),
        ],
        remainder="passthrough",
    )

    return preproc_basic.fit_transform(X)

