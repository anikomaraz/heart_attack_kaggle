import streamlit as st


st.set_page_config(
    page_title="Contact",
    page_icon="👋",
)

linkedin_pic_url = "https://miro.medium.com/v2/resize:fit:640/format:webp/1*EJm3p2XPYATwtPSFpgiLCw.png"


st.markdown(f"""
   ✉️ aniko.maraz[at]gmail[dot]com
    <br>
    <img src="{linkedin_pic_url}" width="20"><a href="https://www.linkedin.com/in/anikomaraz/" target="_blank">LinkedIn</a> 
    <br>
    """, unsafe_allow_html=True)