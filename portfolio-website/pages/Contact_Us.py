import streamlit as st
from send_email import send_mail

st.header("Contact Us!")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter Your Email")
    content = st.text_area("Enter Your message")
    content = content + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        send_mail(content)