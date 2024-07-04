
# Paths to the datasets
TRAIN_DATA_PATH = "data/train.csv"
TEST_DATA_PATH = "data/test.csv"
# MODEL_PATH = "models/model_final_svm.pkl"
MODEL_PATH = "models/xgb_model.pkl"

BEST_TRESHOLD = 0.5306122448979592

# to select variables
CONTINUOUS_VARS = [
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
        "Systolic", # created VAR
        "Diastolic", # created VAR
    ]

CATEGORICAL_VARS = [
        "Diabetes",
        "Family History",
        "Obesity",
        "Alcohol Consumption",
        "Previous Heart Problems",
        "Medication Use",
        "Cholesterol_sample_split", # created VAR
        "Sex",
        "Continent",
        "Diet",
        "Hemisphere",
    ]

LOCAL_INPUT_HIGH = {
    "Patient ID": "BMW7812",
    "Age": 67,
    "Sex": "Male",
    "Cholesterol": 208,
    "Blood Pressure": "158/88",
    "Heart Rate": 72,
    "Diabetes": 0,
    "Family History": 0,
    "Smoking": 1,
    "Obesity": 0,
    "Alcohol Consumption": 0,
    "Exercise Hours Per Week": 4,
    #"Exercise Hours Per Week": 4.16818883544208,
    "Diet": "Average",
    "Previous Heart Problems": 0,
    "Medication Use": 0,
    "Stress Level": 9,
    # "Sedentary Hours Per Day": 6.61500145291406,
    "Sedentary Hours Per Day": 7,
    "Income": 261404,
    # "BMI": 31.2512327252954,
    "BMI": 31,
    "Triglycerides": 286,
    "Physical Activity Days Per Week": 0,
    "Sleep Hours Per Day": 6,
    "Country": "Argentina",
    "Continent": "South America",
    "Hemisphere": "Southern Hemisphere"
}

LOCAL_INPUT_LOW = {
    "Patient ID": "BMW7812",
    "Age": 20,
    "Sex": "Male",
    "Cholesterol": 108,
    "Blood Pressure": "158/88",
    "Heart Rate": 72,
    "Diabetes": 0,
    "Family History": 0,
    "Smoking": 0,
    "Obesity": 0,
    "Alcohol Consumption": 0,
    "Exercise Hours Per Week": 4,
    #"Exercise Hours Per Week": 4.16818883544208,
    "Diet": "Average",
    "Previous Heart Problems": 0,
    "Medication Use": 0,
    "Stress Level": 2,
    # "Sedentary Hours Per Day": 6.61500145291406,
    "Sedentary Hours Per Day": 6,
    "Income": 261404,
    # "BMI": 31.2512327252954,
    "BMI": 21,
    "Triglycerides": 186,
    "Physical Activity Days Per Week": 2,
    "Sleep Hours Per Day": 8,
    "Country": "Argentina",
    "Continent": "South America",
    "Hemisphere": "Southern Hemisphere"
}