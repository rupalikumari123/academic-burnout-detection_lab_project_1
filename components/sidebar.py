import streamlit as st

def show_sidebar():

    st.sidebar.title("📘 About Project")

    st.sidebar.info(
        """
Academic Burnout Detection System

Rule-based AI system predicting burnout
using study habits and lifestyle factors.

Technologies:
• Python
• Streamlit
"""
    )

    st.sidebar.markdown("---")
    st.sidebar.write("👨‍💻 Developed by CSE Students")