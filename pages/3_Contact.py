import streamlit as st


st.set_page_config(
    page_title="Contact",
    page_icon="👋",
)

st.sidebar.header("👋 Contact")

st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    .centered-text h1 {
        font-size: 35px;
        font-weight: bold;
    }
    </style>
    <div class="centered-text">
        <h1>Contact 👋</h1> 
        <br> <br> 

    </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
   ✉️ **aniko.maraz  _[at]_  gmail  _[dot]_  com**
    <br><br> 
    [LinkedIn](https://www.linkedin.com/in/anikomaraz/) 
    <br>
    """, unsafe_allow_html=True)