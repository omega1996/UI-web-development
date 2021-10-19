import streamlit as st
from model import process_image

uploaded_file = st.file_uploader( label='upload file')
if uploaded_file:
    st.write(process_image(uploaded_file.read()))

st.button("Re-run")