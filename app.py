import streamlit as st
import pandas as pd

st.title("Expense Viewer")

uploaded_csv = st.file_uploader("Upload CSV file")

if (uploaded_csv != None):
    df = pd.read_csv(uploaded_csv)
    st.dataframe(df)