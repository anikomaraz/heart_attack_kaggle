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
    </style>
    <div class="centered-text">
        <h1>Welcome to my heart attack risk prediction app. ❤️</h1> 
        <p></p>
        <p></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h2></h2>

    <h3>Quick Summary</h3>

    This project was inspired by the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) competition on Kaggle, with predictions submitted to an ongoing challenge. 
    The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. Focusing on precision, I built and deployed my own model which is currently running in production on this website. I will provide a quick summary of the app's features the following phases, steps and highlights. Please look for the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary) for details on preprocessing, modelling and evaluation.

    1. **Exploratory Data Analysis and Preprocessing:**
       - Explored the dataset thoroughly to uncover patterns and distributions ([see notebook](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)).
       - Implemented extensive preprocessing including feature engineering, encoding, normalization, and balancing to prepare the data for modeling.

    2. **Model Development and Optimization:**
       - Trained and evaluated seven machine learning models including Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting, and Neural Networks.
       - Hyperparameter-tuned the XGBoost, SVM, and the Neural Network models to improve performance metrics.

    3. **Focus on Precision:**
       - However, I argue that the cost of missing truly high-risk cases is high, therefore **precision** is a more suitable metric of model performance.
       - The model with the highest precision was **XGBoost**.
       - To further enhance detection and to account for the lack of positive predictions on the test set, I employed **probability estimation** and found an optimal threshold to increase sensitivity.
       - This strategic adjustment resulted in a higher sensitivity for risk assessment, therefore a better detection for high-risk heart attack cases.
       - Documentation can be found in [this notebook](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb).

    ### Model Deployment
    - The project evolved through multiple versions, culminating in a deployed application hosted on **Google Cloud Platform** with a Streamlit frontend.
    - For more detailed insights, including comprehensive project details, versioning, and visualizations, go to [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary) on this website, or visit my [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle#).
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
    st.markdown(f'<a href="{button["url"]}"><button style="width: 300px; height: 50px;">{button["label"]}</button></a>', unsafe_allow_html=True)


git_icon_url = "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"

# Add GitHub
st.markdown(f"""
    <br>
    For more details, go to the Project's [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle) <img src="{git_icon_url}" width="20">
    <br>
    """, unsafe_allow_html=True)

