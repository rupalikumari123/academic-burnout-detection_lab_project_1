import streamlit as st

def show_sidebar():

    st.sidebar.title("📘 About Project")

    st.sidebar.info(
        """
Academic Burnout Detection System

This AI system predicts student burnout
based on study habits, sleep, stress level,
assignment load, and attendance.

Technologies Used:
• Python
• Machine Learning
• Streamlit
"""
    )

    st.sidebar.markdown("---")
    st.sidebar.write("👨‍💻 Developed by CSE Students")