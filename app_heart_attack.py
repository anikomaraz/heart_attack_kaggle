import streamlit as st

import requests


st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    .centered-text h1 {
        font-size: 45px;  
        font-weight: bold;
    }
    </style>
    <div class="centered-text">
        <h1>Welcome to my heart attack risk prediction app. ❤️</h1>
        <p></p>
        <p></p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<br>
This is a unique opportunity to fake-accurately fake-predict your heart risk based on fake data provided by Kaggle.
<br>
<br>
""", unsafe_allow_html=True)

'''
[Kaggle competition](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) ***
[GitHub repo](https://github.com/anikomaraz/heart_attack_kaggle)
'''

st.markdown("""
<br>
<br>
<br>

""", unsafe_allow_html=True)
# Define default values for features
defaults = {
    "Age": 50,
    "Sex": "Male",
    "Cholesterol": 200,
    "Blood Pressure": "120/90",
    "Heart Rate": 60,
    "Diabetes": 0,
    "Family History": 1,
    "Smoking": 1,
    "Obesity": 1,
    "Alcohol Consumption": 1,
    "Exercise Hours Per Week": 7,
    "Diet": "Unhealthy",
    "Previous Heart Problems": 0,
    "Medication Use": 1,
    "Stress Level": 2,
    "Sedentary Hours Per Day": 1,
    "Income": 184066,
    "BMI": 30,
    "Triglycerides": 63,
    "Physical Activity Days Per Week": 7,
    "Sleep Hours Per Day": 6,
    "Country": "Argentina",
    "Continent": "South America",
    "Hemisphere": "Southern Hemisphere",
    "Heart Attack Risk": 1
}

hemispheres = ["Southern Hemisphere", "Northern Hemisphere"]
continents = ["South America", "Africa", "Asia", "Europe", "North America", "Australia"]
countries = [
    "Argentina", "Nigeria", "Thailand", "Spain", "Germany", "France", "South Africa",
    "Colombia", "Italy", "China", "Vietnam", "United States", "United Kingdom", "Canada",
    "Japan", "New Zealand", "Brazil", "India", "South Korea", "Australia"
]




# Widgets for user inputs with default values
age = st.slider('Age', min_value=18, max_value=100, value=defaults['Age'])
sex = st.selectbox('Sex', ['Male', 'Female'], index=0 if defaults['Sex'] == 'Male' else 1)
cholesterol = st.slider('Cholesterol', min_value=100, max_value=300, value=defaults['Cholesterol'])
blood_pressure = st.selectbox('Blood Pressure', ["90/60", "120/90", "180/140"], index=1 if defaults['Blood Pressure'] == "120/90" else 0)
heart_rate = st.slider('Heart Rate', min_value=50, max_value=100, value=defaults['Heart Rate'])
diabetes = st.selectbox('Diabetes', ['No', 'Yes'], index=1 if defaults['Diabetes'] == 1 else 0)
family_history = st.selectbox('Family History', ['No', 'Yes'], index=1 if defaults['Family History'] == "Yes" else 0)
smoking = st.selectbox('Smoking', ['No', 'Yes'], index=1 if defaults['Smoking'] == 1 else 0)
obesity = st.selectbox('Obesity', ['No', 'Yes'], index=1 if defaults['Obesity'] == 1 else 0)
alcohol_consumption = st.selectbox('Alcohol Consumption', ['No', 'Yes'], index=1 if defaults['Alcohol Consumption'] == 1 else 0)
exercise_hours_per_week = st.slider('Exercise Hours Per Week', min_value=0, max_value=10, value=defaults['Exercise Hours Per Week'])
diet = st.selectbox('Diet', ['Healthy', 'Unhealthy', 'Average'], index=1 if defaults['Diet'] == "Unhealthy" else 0)
previous_heart_problems = st.selectbox('Previous Heart Problems', ['No', 'Yes'], index=1 if defaults['Previous Heart Problems'] == "Yes" else 0)
medication_use = st.selectbox('Medication Use', ['No', 'Yes'], index=1 if defaults['Medication Use'] == 1 else 0)
stress_level = st.slider('Stress Level', min_value=0, max_value=10, value=defaults['Stress Level'])
sedentary_hours_per_day = st.slider('Sedentary Hours Per Day', min_value=0, max_value=24, value=defaults['Sedentary Hours Per Day'])
income = st.number_input('Income per year (rounded to the nearest integer)', value=defaults['Income'])
bmi = st.slider('BMI', min_value=15, max_value=40, value=defaults['BMI'])
triglycerides = st.slider('Triglycerides (basically fat stored in the blood, so high = bad)', min_value=50, max_value=600, value=defaults['Triglycerides'])
physical_activity_days_per_week = st.slider('Physical Activity Days Per Week', min_value=0, max_value=7, value=defaults['Physical Activity Days Per Week'])
sleep_hours_per_day = st.slider('Sleep Hours Per Day', min_value=4, max_value=14, value=defaults['Sleep Hours Per Day'])

# Interactive display for Country, Continent, and Hemisphere
country = st.selectbox('Select a Country', countries)
continent = st.selectbox('Select a Continent', continents)
hemisphere = st.selectbox('Select a Hemisphere', hemispheres)

data_input = {
        'age': age,
        'sex': sex,
        'cholesterol': cholesterol,
        'blood_pressure': blood_pressure,
        'heart_rate': heart_rate,
        'diabetes': diabetes,
        'family_history': family_history,
        'smoking': smoking,
        'obesity': obesity,
        'alcohol_consumption': alcohol_consumption,
        'exercise_hours_per_week': exercise_hours_per_week,
        'diet': diet,
        'previous_heart_problems': previous_heart_problems,
        'medication_use': medication_use,
        'stress_level': stress_level,
        'sedentary_hours_per_day': sedentary_hours_per_day,
        'income': income,
        'bmi': bmi,
        'triglycerides': triglycerides,
        'physical_activity_days_per_week': physical_activity_days_per_week,
        'sleep_hours_per_day': sleep_hours_per_day,
        'country': country,
        'continent': continent,
        'hemisphere': hemisphere
    }
st.markdown("""
<br>
<br>

#### Ready to know your ~fake-heart risk~ fake heart risk?<sup>*</sup>
##### You have: 
""", unsafe_allow_html=True)




# Button to trigger prediction or processing
if st.button('Predict'):
    # Here you would send these values to your FastAPI backend
    # Example HTTP request:
    response = requests.post('http://localhost:8000/predict', json=data_input)

# get prediction from UI
# for local running use: 
    url = "http://127.0.0.1:8000/predict"

# url = 'https://gcloud-5cp25n2jkq-ew.a.run.app/predict'

    params = {'data_input' : data_input}
    response = requests.get(url, params = params)
    heart_attack_prediction = response.json()

    risk = heart_attack_prediction["my_prediction"]

    # Determine the color based on the value of risk
    color = "green" if risk == "LOW RISK" else "red" if risk == "HIGH RISK" else "black"

    # Create the style and dynamically insert the value of risk
    st.markdown(f"""
        <style>
        .big-font {{
            font-size: 30px !important;
            color: {color};
            text-align: center;
            font-weight: bold;
        }}
        </style>
        <p class="big-font">{risk}</p>
        """, unsafe_allow_html=True)


st.markdown("""
<br>
<br>
<br>
""", unsafe_allow_html=True)

# image = requests.post("http://localhost:8079/plot", json = {'stock_prediction': stock_prediction})
# image = requests.post("https://stock-prediction-r-62x2mlrora-ew.a.run.app/plot",
#                      json = {'stock_prediction': stock_prediction})


# st.image(Image.open(BytesIO(image.content)), output_format='png')

st.markdown('''
    <sup>*</sup>Although this model is far from reflecting reality, it should generally point you to the right direction. 
    Want to get high risk? Then live an unhealthy life!
    <br> <br>
    **Find me, blame me:** aniko.maraz[at]gmail.com  
''', unsafe_allow_html=True)
