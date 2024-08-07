import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from utils import load_data, create_new_features, select_features, define_preprocessing_pipeline, train_model, evaluate_model, preprocess, predict

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


    # Select features
    print("Selecting features...")
    X_selected = select_features(df, continuous_vars, categorical_vars)


    # Train-Test split
    print("Performing train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(X_selected, df["Heart Attack Risk"], test_size=0.3,
                                                        random_state=6)

    # Train model
    print("Training XGBClassifier model...")
    preproc_basic = define_preprocessing_pipeline(continuous_vars, categorical_vars)
    model = train_model(X_train, y_train, preproc_basic)

    # Save the model
    model_path = config.MODEL_PATH
    print(f"Saving model to: {model_path}")
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    # Evaluate model
    print("Evaluating model...")
    y_pred_probs = model.predict_proba(preproc_basic.transform(X_test))[:, 1]
    threshold = config.BEST_TRESHOLD
    y_pred_binary = (y_pred_probs > threshold).astype(int)
    precision = precision_score(y_test, y_pred_binary)
    print(f"Precision on test set: {precision}")

    # Load test data
    print(f"Loading test data from: {config.TEST_DATA_PATH}")
    df_input = load_data(config.TEST_DATA_PATH)

    df_input = create_new_features(df_input)
    df_input = select_features(df_input, continuous_vars, categorical_vars)

    # Predict using the saved model
    predictions_probs = model.predict_proba(preproc_basic.transform(df_input))[:, 1]
    predictions = (predictions_probs > threshold).astype(int)

    print(predictions)
