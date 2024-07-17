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
    </style>
    <div class="centered-text">
        <h1>Welcome to my heart attack risk prediction app. ❤️</h1> <br> <br>
        <h3>This is a unique opportunity to fake-predict your heart risk based on fake data.</h3>
        <p></p>
        <p></p>
    </div>
    """, unsafe_allow_html=True)


st.markdown(
    """
    <h2 style="color:#228B22;"></h2>
    
    <h3 style="color:#228B22;">Quick Summary</h3>
    
    This project was inspired by the <a href="https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview">Heart Attack Risk Analysis</a> competition on Kaggle, with predictions submitted to an ongoing challenge. 
    The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. Focusing on precision, I built and deployed my own model which is currently running in production (here). This app features the following phases, steps and highlights:

    <ol>
        <li><b><i style="color:#228B22;">Exploratory Data Analysis and Preprocessing:</i></b>
            <ul>
                <li>Explored the dataset thoroughly to uncover patterns and distributions (<a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb">see notebook</a>).</li>
                <li>Implemented extensive preprocessing including feature engineering, encoding, normalization, and balancing to prepare the data for modeling.</li>
            </ul>
        </li>
        <li><b><i style="color:#228B22;">Model Development and Optimization:</i></b>
            <ul>
                <li>Trained and evaluated seven machine learning models including Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting and Neural Networks.</li>
                <li>Hyperparameter-tuned the XGBoost, SVM and the Neural Network models to improve performance metrics, selected <u><i>XGBoost</i></u> for best performance.</li>
                <li>Given the low number of positive cases on the test set, employed <b>probability estimation</b> and found an optimal threshold to increase sensitivity.</li>
            </ul>
        </li>
        <li><b><i style="color:#228B22;">Focus on Precision:</i></b>
            <ul>
                <li>Although the competition primarily focused on accuracy, I prioritized <b>precision</b> in my model to enhance its capability in correctly identifying positive cases. This strategic adjustment resulted in a higher confidence level for risk assessment.</li>
                <li>Documentation can be found in <a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb">this notebook</a></li>
            </ul>
        </li>
    </ol>

    <h2 style="color:#228B22;">Model Deployment and GitHub Repository</h3>

    - The project evolved through multiple versions, culminating in a deployed application hosted on <u><i>Google Cloud Platform</i></u> with a Streamlit frontend.
    - For more detailed insights, including comprehensive project details, versioning, and visualizations, go to <a href="https://fake-heart-attack.streamlit.app/Technical_summary"</a>Technical Summary on this website, or visit my <a href="https://github.com/anikomaraz/heart_attack_kaggle#">GitHub Repository</a>.
    """,
    unsafe_allow_html=True
)
import streamlit as st

# Define the URLs for the buttons
buttons = [
    {"label": "Go to Prediction 🎯", "url": "https://fake-heart-attack.streamlit.app/Prediction"},
    {"label": "Technical Summary 📈", "url": "https://fake-heart-attack.streamlit.app/Technical_summary"},
    {"label": "Contact 👋", "url": "https://fake-heart-attack.streamlit.app/Contact"},
    {"label": 'GitHub Repository <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20">',
        "url": "https://github.com/anikomaraz/heart_attack_kaggle"}
]

# Create the centered buttons using HTML and CSS
st.markdown(
    """
    <style>
    .center-buttons {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }
    .center-buttons a {
        margin: 10px;
        text-decoration: none;
    }
    .center-buttons button {
        font-size: 16px;
        padding: 10px 20px;
        cursor: pointer;
    }
    </style>
    <div class="center-buttons">
    """ + "\n".join([f'<a href="{button["url"]}" target="_blank"><button>{button["label"]}</button></a>' for button in buttons]) + """
    </div>
    """,
    unsafe_allow_html=True
)





