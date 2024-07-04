from fastapi import FastAPI, HTTPException


import pickle
import pandas as pd

from utils import create_new_features, select_features, apply_probability_threshold
import config

# Load the model
model_path = config.MODEL_PATH
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()



# Endpoint to handle POST requests for prediction
@app.post("/predict")
def predict(data_input: dict):
    try:
        # Get input data from config for local testing
        # data_input = config.LOCAL_INPUT_HIGH

        # Get input data from frontend
        df_input = pd.DataFrame.from_dict(data_input, orient='index').T

        # Preprocessing steps
        df_input = create_new_features(df_input)
        df_input = select_features(df_input, config.CONTINUOUS_VARS, config.CATEGORICAL_VARS)

        # Predict
        probabilities = model.predict_proba(df_input)[:, 1]
        prediction = apply_probability_threshold(probabilities, config.BEST_TRESHOLD)
        prediction_friendly = "HIGH RISK" if prediction == 1 else "LOW RISK"

        # Return prediction result
        return {"my_prediction": prediction_friendly}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


