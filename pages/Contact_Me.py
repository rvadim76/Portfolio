import streamlit as st
import pandas as pd
from Send_Email import send_mail

df = pd.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email Address")
    option = st.selectbox('What topic do you want to discuss?', df["topic"])

    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic {option}
{raw_message}
"""

    button = st.form_submit_button("Submit your message")
    if button:
        send_mail(message)
        st.info("Email was sent successfully.")
