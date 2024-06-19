# preprocessing.py

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def load_data(file_path):
    """
    Loads data from CSV file.

    Returns a pandas.DataFrame: Loaded DataFrame.
    """
    print(f"Loading data from: {file_path}")
    return pd.read_csv(file_path)


def split_blood_pressure(df):
    df[["Systolic", "Diastolic"]] = df["Blood Pressure"].str.split("/", expand=True)
    df["Systolic"] = pd.to_numeric(df["Systolic"])
    df["Diastolic"] = pd.to_numeric(df["Diastolic"])
    df.drop(columns=["Blood Pressure"], inplace=True)

def split_cholesterol_sample(df):
    cholesterol_sample_mean = df["Cholesterol"].mean()
    df["Cholesterol_sample_split"] = np.where(df["Cholesterol"] > cholesterol_sample_mean, 1, 0)


def create_new_features(df):
    df_copy = df.copy()
    split_blood_pressure(df_copy)
    split_cholesterol_sample(df_copy)
    # Add more feature engineering steps as needed

    print(f"Features after creating new features: {df_copy.columns}")
    return df_copy


def select_features(df, continuous_vars, categorical_vars):
    selected_features = continuous_vars + categorical_vars
    if df is None:
        raise ValueError("Input dataframe 'df' is None.")

    if len(selected_features) == 0:
        raise ValueError("No features selected. Check 'continuous_vars' and 'categorical_vars'.")

    selected_features = [col for col in selected_features if col in df.columns]
    return df[selected_features]

def preprocess_data(X_train, X_test, continuous_vars, categorical_vars):
    """
    Applies preprocessing steps to the data using ColumnTransformer.

    Returns preprocessed training and test DataFrames.
    """
    num_transformer = MinMaxScaler()
    cat_transformer = OneHotEncoder(drop="first")

    preproc_basic = ColumnTransformer(
        transformers=[
            ("num", num_transformer, continuous_vars),
            ("cat", cat_transformer, categorical_vars),
        ],
        remainder="passthrough",
    )

    print(f"Features before preprocessing: {X_train.columns}")

    # Fit and transform on training data
    X_train_transformed = preproc_basic.fit_transform(X_train)

    # Transform test data
    X_test_transformed = preproc_basic.transform(X_test)

    # Get the feature names after transformation
    transformed_columns = continuous_vars + cat_transformer.get_feature_names_out(categorical_vars).tolist()
    print(f"Features after preprocessing: {transformed_columns}")

    return X_train_transformed, X_test_transformed, transformed_columns
