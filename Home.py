import streamlit as st

st.set_page_config(
    page_title="Heart Attack App",
    page_icon="💓",
)

st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    .centered-text h1 {
        font-size: 45px;
        font-weight: bold;
    }
    h2, h3 {
        color: #228B22;  /* Green color for headings */
    }
    h5 {
        color: #ff2b2b;  /* Red color for h5 */
    }
    </style>
    <div class="centered-text">
        <h1>Welcome to my heart attack risk prediction app. ❤️</h1> 
        <h5>This is a unique opportunity to fake-predict your heart attack risk. Please note that this model was trained on fake data, so don't take the prediction too seriously. Having said that it should generally point you to the right direction, so if you want to minimise your chance of a heart attack, then live a healthy life!️</h5> 
        <p></p>
        <p></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h2></h2>

    <h3>Quick Summary</h3>

    This project was inspired by the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) competition on Kaggle, with predictions submitted to an ongoing challenge. The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. Focusing on precision, I developed and deployed my own model currently in production on this website. Below is a quick summary of the app's key phases, steps, and highlights. For detailed information on preprocessing, modeling, and evaluation, refer to the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary).

    1. **Exploratory Data Analysis and Preprocessing:**
       - I thoroughly explored the dataset to uncover patterns and distributions ([notebook link](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)).
       - Extensive preprocessing included feature engineering, encoding, normalization, and balancing to prepare data for modeling.

    2. **Model Development and Optimization:**
       - Trained and evaluated seven machine learning models: Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting, and Neural Networks.
       - Hyperparameter-tuned XGBoost, SVM, and Neural Network models to enhance performance metrics.

    3. **Focus on Precision:**
       - I advocate that precision is a better metric than accuracy in this case. Detecting high-risk cases is crucial, which should be the focus of this model instead of classification accuracy as suggested by the competition.
       - Therefore, I optimized model performance for precision and identified **XGBoost** as the highest performing model.
       - Given the low number of predicted positive cases on the test set, I utilized **probability estimation** to adjust sensitivity thresholds, resulting in improved high-risk heart attack detection.
       - Refer to [this notebook](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb) for detailed documentation.

    4. **Model Evaluation**
       - If the model identifies a positive case, it is correct **43% of the time** (=precision).

    ### Model Deployment
    - The project progressed through multiple iterations, culminating in deployment on **Google Cloud Platform** with a Streamlit frontend.
    - For comprehensive project details, versioning, and visualizations, visit the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary) on this website.
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <br>
    <br>
    <h2>Choose an Action:</h2>
    <br>
    """, unsafe_allow_html=True)

# Define the buttons with HTML formatting
buttons = [
    {"label": "Go to <b>Prediction</b> 🎯", "url": "https://fake-heart-attack.streamlit.app/Prediction"},
    {"label": "See the <b>Technical Summary</b> 📈", "url": "https://fake-heart-attack.streamlit.app/Technical_summary"},
    {"label": "<b>Contact Me</b> 👋", "url": "https://fake-heart-attack.streamlit.app/Contact"},
]

# Display buttons
for button in buttons:
    st.markdown(f'<a href="{button["url"]}"><button style="width: 320px; height: 50px;">{button["label"]}</button></a>', unsafe_allow_html=True)

# Add GitHub
git_icon_url = "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"

st.markdown(f"""
    <br>
    For more details, visit the project's <a href="https://github.com/anikomaraz/heart_attack_kaggle" target="_blank">GitHub Repository</a> <img src="{git_icon_url}" width="20">
    <br>
    """, unsafe_allow_html=True)
