import streamlit as st
from send_email import send_email


st.markdown("<h1 style='text-align: center; color: White;'>Contact Me</h1>", unsafe_allow_html=True)


with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email address:")
    raw_message = st.text_area("Enter your message:")

    message =f"""\
Subject: New email from {user_email}

From: {user_email}

{raw_message}
    """

    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent!")



