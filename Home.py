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
        <br>
        <h5>This is a unique opportunity to fake-predict your heart attack risk. Please note that this model was trained on fake data, so don't take the prediction too seriously. Having said that it should generally point you to the right direction, so if you want to minimise your chance of a heart attack, then live a healthy life!️</h5> 
        <p></p>
        <p></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h2></h2>

    <h3>Quick Summary</h3>

    This project was inspired by the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) competition on Kaggle, with predictions submitted to an ongoing challenge. The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. However, I decided develop a better model, that focus on identifying high-risk cases (optimise for precision) instead of correctly identifying all cases (optimised for accuracy, as required by Kaggle). Below is a quick summary of the app's key phases, steps, and highlights. For detailed information on preprocessing, modeling, and evaluation, refer to the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary).

    **Exploratory Data Analysis and Preprocessing:**
    During this phase, I thoroughly explored the dataset to understand distributions and identify missing data. I applied extensive [preprocessing techniques](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb) including feature engineering, encoding, normalization, and balancing to prepare the data for modeling. 

    **Model Development and Optimization:**
    The project involved training and evaluating seven machine learning models: Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting, and Neural Networks. I hyperparameter-tuned the best-performing models, achieving a placement of 46th in the Kaggle competition with a moderate model accuracy of 63.776%. 

    **Focus on Precision:**
    This is where my project took a significant turn. I believe that **precision** is a much better metric for measuring model performance than accuracy (as used by Kaggle). Detecting high-risk cases is crucial because misclassification (i.e., labeling high-risk cases as low-risk) can potentially cost lives. Therefore, I prioritized increasing precision over accuracy. I identified **XGBoost** as the highest-performing model and optimized its parameters for the best performance.

    Furthermore, I noticed that the most accurate models (those placing in the top 5+ in the competition) failed to predict any positive cases in the 1,710 test cases, despite 35% of the training data (N=7,035) being labeled as high-risk. To address this, I enhanced my model's sensitivity by applying **probability estimation** and tuning the threshold. This resulted in a 5% improvement in detection. For detailed documentation, refer to [this notebook](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb).

    **Model Evaluation:**
    If the model identifies a positive case, it is correct **43% of the time** (precision), meaning it will give a false alarm 57% of the time. 

    ### Model Deployment:
    After several iterations, the project culminated in deployment on **Google Cloud Platform** with a Streamlit frontend. For comprehensive code, versioning, and visualizations, please visit the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary) on this website.

    <br>
    Happy faking! 😃
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
