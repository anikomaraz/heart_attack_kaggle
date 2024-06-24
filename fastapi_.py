from fastapi import FastAPI
import pickle

# preprocessing
from utils import create_new_features, select_features
import config

# Load the model
model_path = config.MODEL_PATH
with open(model_path, 'rb') as f:
    model = pickle.load(f)


# get data as user input
data_input_hardcoded = {
    "Patient ID": "RDG0550",
    "Age": 33,
    "Sex": "Male",
    "Cholesterol": 200,
    "Blood Pressure": "129/90",
    "Heart Rate": 48,
    "Diabetes": 0,
    "Family History": 1,
    "Smoking": 1,
    "Obesity": 1,
    "Alcohol Consumption": 1,
    "Exercise Hours Per Week": 7.80768953612279,
    "Diet": "Unhealthy",
    "Previous Heart Problems": 0,
    "Medication Use": 1,
    "Stress Level": 2,
    "Sedentary Hours Per Day": 0.138443450026865,
    "Income": 184066,
    "BMI": 30.4498151376186,
    "Triglycerides": 63,
    "Physical Activity Days Per Week": 7,
    "Sleep Hours Per Day": 6,
    "Country": "Argentina",
    "Continent": "South America",
    "Hemisphere": "Southern Hemisphere",
    "Heart Attack Risk": 1
}

# Define a root `/` endpoint
app = FastAPI()


# streamlit local host: http://localhost:8501
# http://127.0.0.1:8000/predict?stock='AAPL'
# https://stockprediction.streamlit.app/predict?stock=AAPL
@app.get('/predict')
def predict(heart_risk):
    # GET data from API

    # GET hardcoded data for now
    df_input = data_input_hardcoded
    df_input = create_new_features(df_input)
    df_input = select_features(df_input, config.CONTINUOUS_VARS, config.CATEGORICAL_VARS)

    # Predict
    prediction = model.predict(df_input)


    return {
        "input_data": data_input_hardcoded,
        "prediction": prediction


    }


