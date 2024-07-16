import streamlit as st

st.set_page_config(page_title="Quick Summary", page_icon="🌠")

st.sidebar.header("Quick Summary")

st.markdown(
    """
    <h2 style="color:#228B22;">Quick Summary: Heart Attack Risk Analysis</h2>

    This project was developed for the <a href="https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview">Heart Attack Risk Analysis</a> competition on Kaggle, with predictions submitted to an ongoing challenge.
    The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics.

    <h3 style="color:#228B22;">Key Project Phases</h3>

    <ol>
        <li><b><i style="color:#228B22;">Exploratory Data Analysis and Preprocessing:</i></b>
            <ul>
                <li>Explored the dataset thoroughly to uncover patterns and distributions (<a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb">see notebook</a>).</li>
                <li>Implemented extensive preprocessing including feature engineering, encoding, normalization, and balancing to prepare the data for modeling.</li>
            </ul>
        </li>
        <li><b><i style="color:#228B22;">Model Development and Optimization:</i></b>
            <ul>
                <li>Trained and evaluated six machine learning models including Logistic Regression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting and Neural Networks.</li>
                <li>Hyperparameter-tuned the XGBoost, SVM and the Neural Network models to improve performance metrics, selected <u><i>XGBoost</i></u> for best performance.</li>
                <li>Given the low number of positive cases on the test set, employed <u><i>probability estimation</i></u> and found an optimal threshold to increase sensitivity.</li>
            </ul>
        </li>
        <li><b><i style="color:#228B22;">Focus on Precision:</i></b>
            <ul>
                <li>Although the competition primarily focused on accuracy, I prioritized <u><i>precision</i></u> in my model to enhance its capability in correctly identifying positive cases. This strategic adjustment resulted in a higher confidence level for risk assessment.</li>
                <li>Documentation can be found in <a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb">this notebook</a></li>
            </ul>
        </li>
    </ol>

    <h3 style="color:#228B22;">Model Deployment and GitHub Repository</h3>

    - The project evolved through multiple versions, culminating in a deployed application hosted on <u><i>Google Cloud Platform</i></u> with a Streamlit frontend.
    - For more detailed insights, including comprehensive project details, versioning, and visualizations, visit my <a href="https://github.com/anikomaraz/heart_attack_kaggle#">GitHub Repository</a>.
    """,
    unsafe_allow_html=True
)