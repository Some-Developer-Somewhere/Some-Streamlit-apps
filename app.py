import streamlit as st

st.title("Hello World")

uploaded_file = st.file_uploader('File uploader')

if uploaded_file is not None:
    file_content = uploaded_file.read()
    file_content = file_content.decode()

    st.text_area("Contents of the file", value=file_content, height=500)

