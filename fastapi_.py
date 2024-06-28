from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd

# Assuming these imports are needed for preprocessing and model loading
from utils import create_new_features, select_features
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
        # Convert input data to DataFrame (for demonstration)
        df_input = pd.DataFrame([data_input])

        # Preprocessing steps (replace with actual preprocessing functions)
        df_input = create_new_features(df_input)
        df_input = select_features(df_input, config.CONTINUOUS_VARS, config.CATEGORICAL_VARS)

        # Predict
        prediction = model.predict(df_input)[0]
        prediction_friendly = "HIGH RISK" if prediction == 1 else "LOW RISK"

        # Return prediction result
        return {"my_prediction": prediction_friendly}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
