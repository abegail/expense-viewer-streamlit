import streamlit as st
import pandas as pd

st.title("Expense Viewer")

df = pd.read_csv('ExpenseExport.csv')
st.dataframe(df)