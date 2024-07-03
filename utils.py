import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier

def load_data(file_path):
    """
    Loads data from CSV file.
    Returns a pandas.DataFrame.
    """
    print(f"Loading data from: {file_path}")
    return pd.read_csv(file_path)

def split_blood_pressure(df):
    """
    Splits the 'Blood Pressure' column into 'Systolic' and 'Diastolic'.
    """
    df[["Systolic", "Diastolic"]] = df["Blood Pressure"].str.split("/", expand=True)
    df["Systolic"] = pd.to_numeric(df["Systolic"])
    df["Diastolic"] = pd.to_numeric(df["Diastolic"])
    df.drop(columns=["Blood Pressure"], inplace=True)

def split_cholesterol_sample(df):
    """
    Splits the 'Cholesterol' column based on the sample mean.
    """
    cholesterol_sample_mean = df["Cholesterol"].mean()
    df["Cholesterol_sample_split"] = np.where(df["Cholesterol"] > cholesterol_sample_mean, 1, 0)

def create_new_features(df):
    """
    Creates new features in the dataframe.
    """
    df_copy = df.copy()
    split_blood_pressure(df_copy)
    split_cholesterol_sample(df_copy)
    return df_copy

def select_features(df, continuous_vars, categorical_vars):
    """
    Selects the continuous and categorical features from the dataframe.
    """
    selected_features = continuous_vars + categorical_vars
    return df[selected_features]

def define_preprocessing_pipeline(continuous_vars, categorical_vars):
    """
    Defines the preprocessing pipeline for the data.
    Returns a ColumnTransformer: Preprocessing pipeline.
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
    return preproc_basic

def preprocess(df, continuous_vars, categorical_vars, preproc_basic):
    """
    Preprocesses input data using the specified preprocessing pipeline.
    Returns a DataFrame: Preprocessed data.
    """
    print("Starting data preprocessing...")

    # Create new features
    df = create_new_features(df)

    # Select features
    X_selected = select_features(df, continuous_vars, categorical_vars)

    # Preprocess data using the preprocessor
    X_preprocessed = preproc_basic.transform(X_selected)

    return X_preprocessed

def train_model(X_train, y_train, preproc_basic):
    """
    Trains the XGBoost model.
    Returns a Pipeline: Trained XGBoost model pipeline.
    """
    xgb_pipe = Pipeline([
        ("preprocessor", preproc_basic),
        ("classifier", XGBClassifier(random_state=6, objective='binary:logistic')),
    ])
    xgb_pipe.fit(X_train, y_train)
    return xgb_pipe

def apply_probability_threshold(probabilities, threshold):
    """
    Applies a threshold to convert probabilities into binary predictions.
    Returns an ndarray: Binary predictions (0 or 1).
    """
    return (probabilities > threshold).astype(int)

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained model.
    Returns a float: Accuracy score.
    """
    score = model.score(X_test, y_test)
    cv_score = cross_val_score(model, X_test, y_test, cv=5, scoring="precision").mean()
    return score, cv_score

def predict(model, X_preprocessed):
    """
    Makes predictions using the trained model and preprocessed data.
    Returns an ndarray: Predictions.
    """
    probabilities = model.predict_proba(X_preprocessed)[:, 1]  # Probability of positive class
    return probabilities
