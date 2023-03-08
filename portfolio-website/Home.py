import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/cute_me.png", width=380)

with col2:
    st.title("Me on a regular day!")
    content = """
    Hi, Usually, I spend my days learning and coding python, javascript, and some other basic tech.
    This is one of my first portfolio project that I am uploading on github.
    """
    st.info(content)

st.info("Below you can see some of the web app ideas I am working on!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=450)
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=450)