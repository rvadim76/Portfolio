import streamlit as st
import os

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("C:/Users/vrusu/PycharmProjects/portfolio_app/venv/images/photo.png")

with col2:
    st.title("Vadim Rusu")
    content = """ 
    Hi, I am Vadim. I am a Python enthusiast and want to became a professional programmer. I am still learning but
    will be happy to showcase my completed apps here. Please Like and Subscribe, stay tuned!
    """
    #st.write(content)
    st.info(content)


