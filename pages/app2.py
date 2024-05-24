import streamlit as st



page_title="Test reading file"
st.set_page_config(page_title=page_title, page_icon="👋", layout="wide")
st.title(page_title)

uploaded_file = st.file_uploader('File uploader')

if uploaded_file is not None:
    file_content = uploaded_file.read()
    file_content = file_content.decode()

    st.text_area("Contents of the file", value=file_content, height=500)

