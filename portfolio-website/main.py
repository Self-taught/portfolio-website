import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/cute me.png", width=380)

with col2:
    st.title("Me on a regular day!")
    content = """
    Hi, Usually, I spend my days learning and coding python, javascript, and some other basic tech.
    This is one of my first portfolio project that I am uploading on github.
    """
    st.info(content)