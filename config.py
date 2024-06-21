
# Paths to the datasets
TRAIN_DATA_PATH = "data/train.csv"
TEST_DATA_PATH = "data/test.csv"

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