import streamlit as st
import pandas as pd
from utils.predictor import predict_burnout
from components.suggestions import show_suggestions
from components.sidebar import show_sidebar

# Page configuration
st.set_page_config(page_title="Academic Burnout Detection", page_icon="📚")

# Title
st.title("📚 Academic Burnout Detection System")

# Sidebar
show_sidebar()

# Student name
name = st.text_input("Enter Student Name")

st.subheader("Enter Student Details")

# Inputs
study_hours = st.slider("Study Hours per day", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
assignment_load = st.slider("Assignment Load (1-10)", 1, 10, 5)
attendance = st.slider("Attendance Percentage", 0, 100, 75)

# Prediction button
if st.button("Predict Burnout"):

    # FIX: receive BOTH score and level
    burnout_score, level = predict_burnout(
        study_hours,
        sleep_hours,
        stress_level,
        assignment_load,
        attendance
    )

    st.subheader(f"Result for {name if name else 'Student'}")

    # Show burnout level
    if level == "Low":
        st.success("Burnout level-Low 😊")
    elif level == "Medium":
        st.warning("Burnout level-Moderate ⚠️")
    else:
        st.error("Burnout level-High 🚨")

    # Burnout Score Visualization
    st.subheader("Burnout Score")

    percent = min(100, burnout_score)

    st.progress(percent / 100)
    st.metric("Burnout Score", f"{percent:.2f}")

    # Chart visualization
    data = pd.DataFrame({
        "Category": [
            "Study Hours",
            "Sleep Hours",
            "Stress Level",
            "Assignment Load",
            "Attendance"
        ],
        "Value": [
            study_hours,
            sleep_hours,
            stress_level,
            assignment_load,
            attendance
        ]
    })

    st.subheader("Student Activity Overview")
    st.bar_chart(data.set_index("Category"))

    # Suggestions
    show_suggestions(level)

    # Download report
    report = f"""
Academic Burnout Report

Student Name: {name}

Study Hours: {study_hours}
Sleep Hours: {sleep_hours}
Stress Level: {stress_level}
Assignment Load: {assignment_load}
Attendance: {attendance}

Burnout Score: {burnout_score}
Burnout Level: {level}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="burnout_report.txt"
    )

st.markdown("---")
st.write("Developed using Streamlit | Academic Burnout Detection System")