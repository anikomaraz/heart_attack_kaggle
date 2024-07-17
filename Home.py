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
    The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. Focusing on precision, I built and deployed my own model which is currently running in production on this website. I will provide a quick summary of the app's features the following phases, steps and highlights. Please look for the ![Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary) for details on preprocessing, modelling and evaluation.

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
                <li>Hyperparameter-tuned the XGBoost, SVM and the Neural Network models to improve performance metrics.</li>
                
            </ul>
        </li>
        <li><b><i style="color:#228B22;">Focus on Precision:</i></b>
            <ul>
                <li>However, I argue that the cost of missing truly high risk cases is high, therefore <b>precision</> is a more suitable metric of model performance.</li>
                <li>The model with the highest precision was <b>XGBoost</>.</li>
                <li>To further enhance detection and to account for the lack of positive predictions on the test set, I employed <b>probability estimation</b> and found an optimal threshold to increase sensitivity.</li>
                <li>This strategic adjustment resulted in a higher sensitivity for risk assessment, therefore a better detection for high risk heart attack cases.</li>
                <li>Documentation can be found in <a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb">this notebook.</a></li>
            </ul>
        </li>
    </ol>

    <h3 style="color:#228B22;">Model Deployment</h3>

    - The project evolved through multiple versions, culminating in a deployed application hosted on <b>Google Cloud Platform</b> with a Streamlit frontend.
    - For more detailed insights, including comprehensive project details, versioning, and visualizations, go to <a href="https://fake-heart-attack.streamlit.app/Technical_summary">Technical Summary</a> on this website, or visit my <a href="https://github.com/anikomaraz/heart_attack_kaggle#">GitHub Repository</a>.
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <br>
    <br>
     <h2 style="color:#228B22;">Choose an Action:</h2>
    <br>
    """, unsafe_allow_html=True)


# GitHub logo URL
github_logo_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

# Define the buttons with HTML formatting
buttons = [
    {"label": "Go to <b>Prediction</b> 🎯", "url": "https://fake-heart-attack.streamlit.app/Prediction"},
    {"label": "See the <b>Technical Summary</b> 📈", "url": "https://fake-heart-attack.streamlit.app/Technical_summary"},
    {"label": "<b>Contact Me</b> 👋", "url": "https://fake-heart-attack.streamlit.app/Contact"},
]

# Display buttons
for button in buttons:
    st.button(button["label"], on_click=button["url"], unsafe_allow_html=True)

# Display GitHub repository link with logo
st.markdown(
    f"""
    Visit the Project's [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle) 
    <br>
    <img src="{github_logo_url}" alt="GitHub Logo" width="20">
    """, unsafe_allow_html=True)


