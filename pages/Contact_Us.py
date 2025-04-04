import streamlit as st

from send_email import send_email
st. header ("Contact Me")
contact_details = """You can reach out to me through the following channels:"""

with st.form(key = "my_emailForm"):
    user_email = st.text_input("Your email address:")
    raw_message = st.text_area("Your Message")
    message = f"""\ 
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your Email was sent successfully!")


