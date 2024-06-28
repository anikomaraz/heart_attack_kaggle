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
This is a unique opportunity to fake-predict your heart risk based on fake data provided by Kaggle.  
All you need to do is fake-fill-out the questionnaire below. I save you some work by providing default values which you are welcome to modify.  

[Kaggle competition](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview)  
[GitHub repo](https://github.com/anikomaraz/heart_attack_kaggle)
""", unsafe_allow_html=True)

st.markdown("""
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

# Mapping categorical inputs to numeric values
data_input = {
    'Age': age,
    'Heart Rate': heart_rate,
    'Exercise Hours Per Week': exercise_hours_per_week,
    'Stress Level': stress_level,
    'Sedentary Hours Per Day': sedentary_hours_per_day,
    'Income': income,
    'BMI': bmi,
    'Triglycerides': triglycerides,
    'Physical Activity Days Per Week': physical_activity_days_per_week,
    'Sleep Hours Per Day': sleep_hours_per_day,
    'Blood Pressure': blood_pressure,
    'Diabetes': 1 if diabetes == 'Yes' else 0,
    'Family History': 1 if family_history == 'Yes' else 0,
    'Obesity': 1 if obesity == 'Yes' else 0,
    'Alcohol Consumption': 1 if alcohol_consumption == 'Yes' else 0,
    'Previous Heart Problems': 1 if previous_heart_problems == 'Yes' else 0,
    'Medication Use': 1 if medication_use == 'Yes' else 0,
    'Cholesterol': cholesterol,
    'Sex': sex,
    'Continent': continent,
    'Diet': diet,
    'Hemisphere': hemisphere,
}

st.markdown("""
<br>
<br>

#### Ready to know your ~fake-heart risk~ fake heart risk?<sup>*</sup>
##### You have: 
""", unsafe_allow_html=True)

# Button to trigger prediction or processing
if st.button('Predict'):
    docker_url = 'https://heart-attack-app-33s7xrm4hq-od.a.run.app/predict'

    try:
        response = requests.post(docker_url, json=data_input)

        if response.status_code == 200:
            heart_attack_prediction = response.json()
            # st.write(f"Response JSON: {heart_attack_prediction}")
            prediction = heart_attack_prediction.get('my_prediction', 'No prediction returned')

            # Determine the color based on the prediction
            color = "green" if prediction == "LOW RISK" else "red" if prediction == "HIGH RISK" else "black"

            # Display prediction
            st.markdown(f"""
                    <style>
                    .big-font {{
                        font-size: 30px !important;
                        color: {color};
                        text-align: center;
                        font-weight: bold;
                    }}
                    </style>
                    <p class="big-font">{prediction}</p>
                    """, unsafe_allow_html=True)
        else:
            st.error('Failed to get prediction.')
            #st.write(f"Error details: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f'Error: {e}')

st.markdown("""
<br>
<br>
<br>
""", unsafe_allow_html=True)

st.markdown('''
    <sup>*</sup>Although this model is far from reflecting reality, it should generally point you to the right direction. 
    Want to get high risk? Then live an unhealthy life! 
    <br> <br>
    **Find me, blame me:** aniko.maraz[at]gmail.com  
''', unsafe_allow_html=True)