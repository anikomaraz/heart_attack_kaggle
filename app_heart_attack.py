import streamlit as st

import pandas as pd
import numpy as np

import requests
import urllib.parse

from PIL import Image
from io import BytesIO
import json

'''
# Welcome to my heart attack risk prediction app. :heart:

This is a unique opportunity to fake-accurately fake-predict your heart risk based on fake data provided by Kaggle. 

:sunglasses:
'''

'''
[Kaggle competition](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview)
[GitHub repo](https://github.com/anikomaraz/heart_attack_kaggle)
'''
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

hemispheres = ["Southern Hemisphere", "Northern Hemisphere"]
continents = ["South America", "Africa", "Asia", "Europe", "North America", "Australia"]
countries = [
    "Argentina", "Nigeria", "Thailand", "Spain", "Germany", "France", "South Africa",
    "Colombia", "Italy", "China", "Vietnam", "United States", "United Kingdom", "Canada",
    "Japan", "New Zealand", "Brazil", "India", "South Korea", "Australia"
]


# Streamlit app UI
st.title('Heart Risk Predictor')


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
income = st.number_input('Income', value=defaults['Income'])
bmi = st.slider('BMI', min_value=15, max_value=40, value=defaults['BMI'])
triglycerides = st.slider('Triglycerides', min_value=50, max_value=600, value=defaults['Triglycerides'])
physical_activity_days_per_week = st.slider('Physical Activity Days Per Week', min_value=0, max_value=7, value=defaults['Physical Activity Days Per Week'])
sleep_hours_per_day = st.slider('Sleep Hours Per Day', min_value=4, max_value=14, value=defaults['Sleep Hours Per Day'])

# Interactive display for Country, Continent, and Hemisphere
country = st.selectbox('Select a Country', countries)
continent = st.selectbox('Select a Continent', continents)
hemisphere = st.selectbox('Select a Hemisphere', hemispheres)

'''
#### Ready to know your ~fake-heart~ fake heart risk? 
'''
# Button to trigger prediction or processing
if st.button('Predict'):
    # Here you would send these values to your FastAPI backend
    # Example HTTP request:
    # response = requests.post('http://localhost:8000/predict', json={
    #     'age': age, 'sex': sex, 'cholesterol': cholesterol, 'blood_pressure': blood_pressure,
    #     'heart_rate': heart_rate, 'diabetes': diabetes, 'family_history': family_history,
    #     'smoking': smoking, 'obesity': obesity, 'alcohol_consumption': alcohol_consumption,
    #     'exercise_hours_per_week': exercise_hours_per_week, 'diet': diet,
    #     'previous_heart_problems': previous_heart_problems, 'medication_use': medication_use,
    #     'stress_level': stress_level, 'sedentary_hours_per_day': sedentary_hours_per_day,
    #     'income': income, 'bmi': bmi, 'triglycerides': triglycerides,
    #     'physical_activity_days_per_week': physical_activity_days_per_week,
    #     'sleep_hours_per_day': sleep_hours_per_day
    # })

# Optionally, display results or feedback from the backend response


# get price prediction from UI
# for local running use: 
# url = "http://127.0.0.1:8000/predict"

url = 'https://gcloud-5cp25n2jkq-ew.a.run.app/predict'

params = {'stock' : stock_name}
response = requests.get(url, params = params)
stock_prediction = response.json() 


#st.write(stock_prediction)


'''
### This is what you can expect
'''

# image = requests.post("http://localhost:8079/plot", json = {'stock_prediction': stock_prediction})
image = requests.post("https://stock-prediction-r-62x2mlrora-ew.a.run.app/plot", 
                      json = {'stock_prediction': stock_prediction})


st.image(Image.open(BytesIO(image.content)), output_format='png')


st.markdown('''
            **Blame me, find me:** aniko.maraz[at]gmail.com  
            ''')
