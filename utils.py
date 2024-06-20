import numpy as np
import pandas as pd

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


def preprocess(df, continuous_vars, categorical_vars, preproc_basic):
    """
    Preprocesses input data using the specified preprocessing pipeline.
    Returns a DataFrame: Preprocessed data.
    """
    print("Starting data preprocessing...")

    # Create new features
    df = create_new_features(df)
    print(f"Features after creating new features: {df.columns}")

    # Select features
    X_selected = select_features(df, continuous_vars, categorical_vars)
    print(f"Selected features: {X_selected.columns}")
    print(f"Number of selected features: {X_selected.shape[1]}")

    # Preprocess data using the preprocessor
    X_preprocessed = preproc_basic.transform(X_selected)

    # Ensure X_preprocessed is a DataFrame for better understanding of the columns.
    X_preprocessed_df = pd.DataFrame(X_preprocessed, columns=preproc_basic.get_feature_names_out())
    print(f"Features before preprocessing: {X_selected.columns}")
    print(f"Features after preprocessing: {X_preprocessed_df.columns}")
    print(f"Shape of preprocessed data: {X_preprocessed_df.shape}")

    return X_preprocessed_df


def predict(model, X_preprocessed):
    """
    Makes predictions using the trained model and preprocessed data.
    Returns an ndarray: Predictions.
    """
    print("Making predictions...")
    predictions = model.predict(X_preprocessed)
    return predictions
