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



# read in data
df_raw_train = pd.read_csv("data/train.csv")

# create new features
df = df_raw_train.copy()

split_blood_pressure(df=df)
split_cholesterol_sample(df=df)


# Define features and target
X = df.drop(columns="Heart Attack Risk")
y = df["Heart Attack Risk"]

# Opt-in continuous and categorical variables
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

X_selected = X[continuous_vars + categorical_vars]




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









X_train_sentiments = merged_features.rename(columns= {'News_Count':'news_count', 
                                                         'News_Sentiment': 'news_sentiment', 
                                                         'Tweet_Count': 'tweet_count', 
                                                         'Tweet_Sentiment': 'tweet_sentiment'})
# X_train_sentiments should contain ["news_count", "news_sentiment", "tweet_count", "tweet_sentiment"]], shape is (batch_size, 30, 4)
X_train_sentiments.shape
# model = load_model("model_combined_1.h5")
stock_prediction_14 = model.predict([X_train_stocks, X_train_sentiments])[0].tolist()
stock_prediction_14
# X_train_stocks should contain ["open", "high", "low", "close", "adjusted_close", "volume"], shape is (batch_size, 30, 6)
# X_train_sentiments should contain ["news_count", "news_sentiment", "tweet_count", "tweet_sentiment"]], shape is (batch_size, 30, 4)

# Data should be for the last 30 days
