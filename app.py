import streamlit as st

st.title("Agent Hackathon Demo")
user_input = st.text_input("Ask something:")
if user_input:
    st.write("You asked:", user_input)
