import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

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


# get features with self-defined functions
from function_defs.split_blood_pressure import split_blood_pressure
from function_defs.split_cholesterol_sample import split_cholesterol_sample

# get model 
from keras.models import load_model
model = load_model('model_combined_1.h5')





################# MAIN CODE #################

if __name__ == "__main__":
    file_path = "data/train.csv"
    continuous_vars = [
        "Age",
        # "Cholesterol",
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
        # "Exercise Total",
        # "Systolic_Diastolic_Ratio",
    ]

    categorical_vars = [
        "Diabetes",
        "Family History",
        "Obesity",
        "Alcohol Consumption",
        "Previous Heart Problems",
        "Medication Use",
        "Cholesterol_sample_split",
        # "Smoking",
        "Sex",
        "Continent",
        "Diet",
        "Hemisphere",
        # "Country",
        ]

    # Load data
    df_raw_train = load_data(file_path)

    # Create new features
    df = create_new_features(df_raw_train)

    # Select features
    X_selected = select_features(df, continuous_vars, categorical_vars)


    num_transformer = MinMaxScaler()
    cat_transformer = OneHotEncoder(drop="first")

    X_preprocessed = preprocess_data(X_selected, num_transformer, cat_transformer)






# Define preprocessing steps for continuous and categorical features
num_transformer = MinMaxScaler()
cat_transformer = OneHotEncoder(drop="first")

preproc_basic = ColumnTransformer(
    transformers=[
        ("num", num_transformer, continuous_vars),
        ("cat", cat_transformer, categorical_vars),
    ],
    remainder="passthrough",
)


# Create pipelines for each classifier

svm_pipe = make_pipeline(preproc_basic, SVC(random_state=6))


# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(
    X_selected, y, test_size=0.3, random_state=6
)


svm_pipe.fit(X_train, y_train)
score = svm_pipe.score(X_test, y_test)

# Cross-validate the pipeline
cv_score = cross_val_score(svm_pipe, X_train, y_train, cv=5, scoring="accuracy").mean()
print(f"Cross-validated accuracy for svm_pipe: {cv_score}")

# Fit preprocessing on the entire dataset
X_train_preprocessed = preproc_basic.fit_transform(X_train)

# Convert the transformed data to a DataFrame
X_train_preprocessed_df = pd.DataFrame(
    X_train_preprocessed,
    columns=continuous_vars
    + list(
        preproc_basic.named_transformers_["cat"].get_feature_names_out(categorical_vars)
    ),
)

df_kaggle_test = pd.read_csv("data/test.csv")  # read in test data provided by Kaggle

# preprocess input data
df_kaggle_test = df_kaggle_test.copy()

split_blood_pressure(df=df_kaggle_test)
split_cholesterol_sample(df=df_kaggle_test)

X_df_kaggle_test_selected = df_kaggle_test[continuous_vars + categorical_vars]

# Create SVM pipeline with best parameters
best_params = {"C": 0.0001, "kernel": "linear", "gamma": "scale", "class_weight": None}

svm_pipe = Pipeline(
    [
        ("preprocessor", preproc_basic),
        ("classifier", SVC(**best_params, random_state=6)),
    ]
)

# Train the SVM model on the entire preprocessed training dataset
svm_pipe.fit(X_selected, y)


prediction = svm_pipe.predict(X_df_kaggle_test_selected)
prediction


