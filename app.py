import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Expense Viewer")

df = pd.read_csv('ExpenseExport.csv')

category_sum = df.groupby('Category')['Cost'].sum()
category_sum_df = category_sum.reset_index()
category_sum_df.columns = ['Category', 'Total']

st.dataframe(category_sum_df)

fig = px.pie(category_sum_df, values='Total', names='Category')
st.plotly_chart(fig)