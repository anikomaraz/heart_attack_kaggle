import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import utils
import config



if __name__ == "__main__":
    file_path = config.TRAIN_DATA_PATH

    continuous_vars = config.CONTINUOUS_VARS

    categorical_vars = config.CATEGORICAL_VARS



    # Load data
    print(f"Loading data from: {file_path}")
    df_raw_train = load_data(file_path)

    # Create new features
    print("Creating new features...")
    df = create_new_features(df_raw_train)
    print(f"Features after creating new features: {df.columns}")

    # Select features
    print("Selecting features...")
    X_selected = select_features(df, continuous_vars, categorical_vars)
    print(f"Selected features: {X_selected.columns}")

    # Train-Test split
    print("Performing train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(X_selected, df["Heart Attack Risk"], test_size=0.3,
                                                        random_state=6)

    # Train model
    print("Training model...")
    preproc_basic = define_preprocessing_pipeline(continuous_vars, categorical_vars)
    model = train_model(X_train, y_train, preproc_basic)

    # Evaluate model
    print("Evaluating model...")
    score, cv_score = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {score}, Cross-validated Accuracy: {cv_score}")

    # Load test data
    print(f"Loading test data from: {config.TEST_DATA_PATH}")
    df_input = load_data(config.TEST_DATA_PATH)

    # Preprocess test data
    X_preprocessed = preprocess(df_input, continuous_vars, categorical_vars, preproc_basic)

    # Predict
    predictions = predict(model, X_preprocessed)
    print(predictions)
