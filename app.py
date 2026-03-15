import streamlit as st
import pandas as pd
from utils.predictor import predict_burnout
from components.suggestions import show_suggestions
from components.sidebar import show_sidebar

st.set_page_config(page_title="Academic Burnout Detection", page_icon="📚")

st.title("📚 Academic Burnout Detection System")

show_sidebar()

# Student Name
name = st.text_input("Enter Student Name")

st.subheader("Enter Student Details")

study_hours = st.slider("Study Hours per day", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
assignment_load = st.slider("Assignment Load (1-10)", 1, 10, 5)
attendance = st.slider("Attendance Percentage", 0, 100, 75)

# Prediction
if st.button("Predict Burnout"):

    level, burnout_score = predict_burnout(
        study_hours,
        sleep_hours,
        stress_level,
        assignment_load,
        attendance
    )

    st.subheader(f"Result for {name if name else 'Student'}")

    # Result Display
    if level == 0:
        st.success("Low Burnout 😊")
    elif level == 1:
        st.warning("Moderate Burnout ⚠️")
    else:
        st.error("High Burnout 🚨")

    # Score Meter
    st.subheader("Burnout Score")
    percent = min(100, burnout_score)
    st.progress(percent / 100)
    st.metric("Burnout Score", f"{percent:.2f}")

    # Chart
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

    # Download Report
    report = f"""
Academic Burnout Report

Student Name: {name}

Study Hours: {study_hours}
Sleep Hours: {sleep_hours}
Stress Level: {stress_level}
Assignment Load: {assignment_load}
Attendance: {attendance}

Burnout Score: {burnout_score:.2f}
Burnout Level: {['Low','Medium','High'][level]}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="burnout_report.txt"
    )

st.markdown("---")
st.write("Developed using Streamlit | Academic Burnout Detection System")