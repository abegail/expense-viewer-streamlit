import streamlit as st
import pandas as pd

st.title("Expense Viewer")

df = pd.read_csv('ExpenseExport.csv')

category_sum = df.groupby('Category')['Cost'].sum()
category_sum_df = category_sum.reset_index()
category_sum_df.columns = ['Category', 'Total']

st.dataframe(category_sum_df)