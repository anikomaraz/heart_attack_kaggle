# train.py

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, cross_val_score
from preprocessing import load_data, create_new_features, select_features, preprocess_data
import config


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
        remainder="drop"  # Adjust remainder handling if needed
    )
    return preproc_basic


def train_model(X_train, y_train, preproc_basic):
    """
    Trains the SVM model.
    Returns a Pipeline: Trained SVM model pipeline.
    """
    svm_pipe = Pipeline([
        ("preprocessor", preproc_basic),
        ("classifier", SVC(random_state=6)),
    ])
    svm_pipe.fit(X_train, y_train)
    return svm_pipe


def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained model.
    Returns a float: Accuracy score.
    """
    score = model.score(X_test, y_test)
    cv_score = cross_val_score(model, X_test, y_test, cv=5, scoring="accuracy").mean()
    return score, cv_score


def preprocess_and_predict(model, df_input, continuous_vars, categorical_vars):
    """
    Preprocesses input data and makes predictions using the trained model.
    Returns an ndarray: Predictions.
    """
    print("Starting data preprocessing...")

    # Create new features if necessary
    # df_input = create_new_features(df_input)
    print(f"Features after creating new features: {df_input.columns}")

    # Select features
    X_input_selected = select_features(df_input, continuous_vars, categorical_vars)
    print(f"Selected features: {X_input_selected.columns}")
    print(f"Number of selected features: {X_input_selected.shape[1]}")

    # Preprocess data
    preproc_basic = define_preprocessing_pipeline(continuous_vars, categorical_vars)
    X_input_preprocessed = preproc_basic.fit_transform(X_input_selected)
    print(f"Features before preprocessing: {X_input_selected.columns}")

    # Ensure X_input_preprocessed is a DataFrame for better understanding of the columns.
    X_input_preprocessed_df = pd.DataFrame(X_input_preprocessed, columns=preproc_basic.get_feature_names_out())
    print(f"Features after preprocessing: {X_input_preprocessed_df.columns}")

    predictions = model.predict(X_input_preprocessed)
    return predictions


if __name__ == "__main__":
    file_path = config.TRAIN_DATA_PATH

    continuous_vars = [
        "Age",
        "Heart Rate",
        "Exercise Hours Per Week",
        "Stress Level",
        "Sedentary Hours Per Day",
        "Income",
        "BMI",
        "Triglycerides",
        "Physical Activity Days Per Week",
        "Sleep Hours Per Day",
        "Systolic",
        "Diastolic",
    ]

    categorical_vars = [
        "Diabetes",
        "Family History",
        "Obesity",
        "Alcohol Consumption",
        "Previous Heart Problems",
        "Medication Use",
        "Cholesterol_sample_split",
        "Sex",
        "Continent",
        "Diet",
        "Hemisphere",
    ]

    # Load data
    print(f"Loading data from: {file_path}")
    df_raw_train = load_data(file_path)

    # Create new features
    print("Creating new features...")
    df = create_new_features(df_raw_train)
    print(f"Features after creating new features: {df.columns}")

    # Select features
    print("Selecting features...")
    print(f"Continuous variables: {continuous_vars}")
    print(f"Categorical variables: {categorical_vars}")
    X_selected = select_features(df_raw_train, continuous_vars, categorical_vars)

    # Train-Test split
    print("Performing train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(X_selected, df["Heart Attack Risk"], test_size=0.3,
                                                        random_state=6)

    # Train model
    print("Training model...")
    model = train_model(X_train, y_train, define_preprocessing_pipeline(continuous_vars, categorical_vars))

    # Evaluate model
    print("Evaluating model...")
    score, cv_score = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {score}, Cross-validated Accuracy: {cv_score}")

    # Load test data
    print(f"Loading test data from: {config.TEST_DATA_PATH}")
    df_input = load_data(config.TEST_DATA_PATH)

    # Predict
    print("Making predictions...")
    predictions = preprocess_and_predict(model, df_input, continuous_vars, categorical_vars)
    print(predictions)
