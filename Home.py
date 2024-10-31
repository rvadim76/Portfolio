import streamlit as st
import os
import pandas

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

content2 = """
Below you can find some of the apps I have built in Phyton (more to come). Please feel free to contact me!
"""

st.write(content2)

# col3, empty_col, col4 = st.columns(3)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("C:/Users/vrusu/PycharmProjects/portfolio_app/venv/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("C:/Users/vrusu/PycharmProjects/portfolio_app/venv/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("C:/Users/vrusu/PycharmProjects/portfolio_app/venv/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


