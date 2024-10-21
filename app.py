import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Expense Viewer")

df = pd.read_csv('ExpenseExport.csv')

category_sum = df.groupby('Category')['Cost'].sum()
category_sum_df = category_sum.reset_index()
category_sum_df.columns = ['Category', 'Total']

category_to_bucket = {
    'Clothing': 'Fixed Costs',
    'Debt Repayment': 'Fixed Costs',
    'Eating Out': 'Guilt-free Spending',
    'Food': 'Fixed Costs',
    'Giving': 'Guilt-free Spending',
    'Groceries': 'Fixed Costs',
    'Housing': 'Fixed Costs',
    'Meds': 'Fixed Costs',
    'Pets': 'Fixed Costs',
    'Subscriptions': 'Fixed Costs',
    'Transportation': 'Fixed Costs',
    'Travel': 'Guilt-free Spending',
    'Wants': 'Guilt-free Spending',
    'Emergency': 'Emergency Spend',
    'Taxes': 'Tax',
}

df['Buckets'] = df['Category'].map(category_to_bucket)
aggregated_df = df.groupby('Buckets').sum().reset_index()

fig = px.pie(category_sum_df, values='Total', names='Buckets')

st.dataframe(category_sum_df)

# fig = px.pie(category_sum_df, values='Total', names='Category')
# st.plotly_chart(fig)