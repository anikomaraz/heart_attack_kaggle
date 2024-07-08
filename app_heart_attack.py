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
Please enter your fake data - you are welcome to modify the default values.


""", unsafe_allow_html=True)

st.markdown("""
<br>
<br>
""", unsafe_allow_html=True)

# Define default values for features
defaults = {
    "Age": 36,
    "Sex": "Male",
    "Cholesterol": 133,
    "Blood Pressure": "161/90",
    "Heart Rate": 97,
    "Diabetes": 1,
    "Family History": 0,
    "Smoking": 1,
    "Obesity": 1,
    "Alcohol Consumption": 1,
    "Exercise Hours Per Week": 4,
    "Diet": "Healthy",
    "Previous Heart Problems": 1,
    "Medication Use": 0,
    "Stress Level": 10,
    "Sedentary Hours Per Day": 10,
    "Income": 223132,
    "BMI": 22,
    "Triglycerides": 605,
    "Physical Activity Days Per Week": 5,
    "Sleep Hours Per Day": 10,
    "Country": "Canada",
    "Continent": "North America",
    "Hemisphere": "Northern Hemisphere",
    "Heart Attack Risk": 1
}


hemispheres = ["Southern Hemisphere", "Northern Hemisphere"]
continents = ["South America", "Africa", "Asia", "Europe", "North America", "Australia"]
countries = [
    "Argentina", "Nigeria", "Thailand", "Spain", "Germany", "France", "South Africa",
    "Colombia", "Italy", "China", "Vietnam", "United States", "United Kingdom", "Canada",
    "Japan", "New Zealand", "Brazil", "India", "South Korea", "Australia", "Afghanistan",
    "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Armenia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Central African Republic",
    "Chad", "Chile", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "Gabon", "Gambia", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "Indonesia", "Iran", "Iraq",
    "Ireland", "Israel", "Ivory Coast", "Jamaica", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo",
    "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Nicaragua", "Niger", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Sudan", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "Uruguay", "Uzbekistan",
    "Vanuatu", "Vatican City", "Venezuela", "Yemen", "Zambia", "Zimbabwe"
]


# Widgets for user inputs with default values
age = st.slider('Age', min_value=18, max_value=100, value=defaults['Age'])
sex = st.selectbox('Sex', ['Male', 'Female'], index=0 if defaults['Sex'] == 'Male' else 1)
cholesterol = st.slider('Cholesterol', min_value=100, max_value=300, value=defaults['Cholesterol'])

options_blood_pressure = ["90/60", "120/90", "180/140", "158/88"]
selected_index = next((i for i, option in enumerate(options_blood_pressure) if option == defaults['Blood Pressure']), 0)
blood_pressure = st.selectbox('Blood Pressure', options_blood_pressure, index=selected_index)
# blood_pressure = st.selectbox('Blood Pressure', ["90/60", "120/90", "180/140", "158/88"], index=1 if defaults['Blood Pressure'] == "158/88" else 0)

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
income = st.number_input('Income per year', value=defaults['Income'])
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

    except requests.exceptions.RequestException as e:
        st.error(f'Error: {e}')

st.markdown("""
<br>
<br>
<br>
""", unsafe_allow_html=True)

st.markdown('''
    <i>The estimation should be done in ~5 seconds, please be patient.</i>
    <br><br>
    <sup>*</sup>Although this model is far from reflecting reality, it should generally point you to the right direction.
    Want to get high risk? Then live an unhealthy life!
    <br> <br>
    To learn more about the project's technical background, please visit my [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle).
    <br> <br>
    **Find me, blame me:** aniko.maraz[at]gmail.com
''', unsafe_allow_html=True)


# Sidebar
st.sidebar.markdown(
    """

    **Project Overview: Heart Attack Risk Analysis**

    This project was developed for the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) competition on Kaggle, with predictions submitted to an ongoing challenge.

    **Key Project Phases**

    1. **Exploratory Data Analysis and Preprocessing:**
       - Explored the dataset thoroughly to uncover patterns and distributions ([see link](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)).
       - Implemented extensive preprocessing including feature engineering, encoding, normalization, and balancing to prepare the data for modeling.

    2. **Model Development and Optimization:**
       - Trained and evaluated six machine learning models including Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, and Gradient Boosting.
       - Hyperparameter-tuned the XGBoost and SVM models to improve performance metrics, selected XGBoost for best performance.

    3. **Focus on Precision**

       Although the competition primarily focused on accuracy, I prioritized <b>precision</b> in my model to enhance its capability in correctly identifying positive cases. This strategic adjustment resulted in a higher confidence level for risk assessment.

    **Model Deployment and GitHub Repository**

    - The project evolved through multiple versions, culminating in a deployed application hosted on Google Cloud Platform with a Streamlit frontend.
    - For more detailed insights, including comprehensive project details, versioning, and visualizations, visit my [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle#).

    """,
    unsafe_allow_html=True
)

