import streamlit as st

st.set_page_config(
    page_title="Heart Attack App",
    page_icon="💓",
)

st.sidebar.header("💓 Home")

st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    .centered-text h1 {
        font-size: 45px;
        font-weight: bold;
    }
    h2, h3, h6 {
        color: #228B22;  /* Green color for headings */
    }
    h5 {
        color: #ff2b2b;  /* Red color for h5 */
    }
    
    </style>
    <div class="centered-text">
        <h1>Welcome to my heart attack risk prediction app. ❤️</h1> 
        <br> <br> 
       
    </div>
    """, unsafe_allow_html=True)


disclaimer = ("Please note that this model was trained on fake data, so don't take the prediction too seriously. "
              "Having said that it should generally point you to the right direction. "
              "If you want to minimise your chance of a heart attack, then live a healthy life!️")

st.warning(disclaimer)

st.markdown(
    """
       
    <br> <br>
    <h3>Quick Summary</h3>

    **:green[The Challenge]:** This project was inspired by the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) competition on Kaggle, with predictions submitted to an ongoing challenge. 
    The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. 
    After preprocessing the data, I trained and evaluated 7 machine learning models, fine-tuned the best performing ones and achieved a placement of :blue-background[46th in the Kaggle competition]. 
    
    **:green[Focus on Precision]:**
    The Kaggle competition was scored on model _accuracy_ that reflects the model's ability to correctly label both true and false cases. 
    However, in this particular case, missing a high-risk (positive) case of heart attack could be fatal. 
    To mitigate this risk and ensure high-risk cases are captured as diligently as possible, I prioritized :blue-background[**precision** as a measure of goodness of fit]. 
    Optimizing for precision allows for more sensitive detection of high-risk cases in production, potentially saving lives. 
    
    
    **:green[Model and Evaluation]:** To further enhance the model's sensitivity, I opted for :blue-background[probability estimation] and found the best-scoring model on precision to be the :blue-background[XGBoost] model. Following fine-tuning this model achieved a precision of 0.4286. 
    This means that if the model identifies a positive case, it is :blue-background[**correct 43% of the time**] (precision), meaning it will give a false alarm 57% of the time.
    
    **:green[Model Deployment]:** After several iterations, the project culminated in deployment on :blue-background[Google Cloud Platform] with a Streamlit frontend. 

      
    For detailed information on preprocessing, modeling, evaluation and visualisations refer to the [Technical Summary](https://fake-heart-attack.streamlit.app/Technical_summary).

     
    
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
