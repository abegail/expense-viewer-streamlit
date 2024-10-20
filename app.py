import streamlit as st

st.title("Streamlit Test")

user_input = st.text_input("Enter some text:")
st.write("You entered: ", user_input)