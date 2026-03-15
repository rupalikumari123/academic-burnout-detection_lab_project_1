# import streamlit as st
# from utils.predictor import predict_burnout
# from components.suggestions import show_suggestions
# from components.sidebar import show_sidebar

# # Page settings
# st.set_page_config(page_title="Academic Burnout Detection", page_icon="📚")

# # Title
# st.title("📚 Academic Burnout Detection System")

# # Sidebar
# show_sidebar()

# # Input section
# st.subheader("Enter Student Details")

# study_hours = st.slider("Study Hours per day", 0, 12, 5)
# sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
# stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)

# # Extra inputs (not used in prediction)
# assignment_load = st.slider("Assignment Load (1-10)", 1, 10, 5)
# screen_time = st.slider("Screen Time (hours)", 0, 12, 4)

# # Prediction button
# if st.button("Predict Burnout"):

#     # Send only 3 inputs to model
#     prediction = predict_burnout(
#         study_hours,
#         sleep_hours,
#         stress_level
#     )

#     # Show result
#     if prediction == 0:
#         st.success("Low Burnout 😊")

#     elif prediction == 1:
#         st.warning("Moderate Burnout ⚠️")

#     else:
#         st.error("High Burnout 🚨")

#     # Show suggestions
#     show_suggestions(prediction)




import streamlit as st
import pandas as pd
from utils.predictor import predict_burnout
from components.suggestions import show_suggestions
from components.sidebar import show_sidebar

# Page Config
st.set_page_config(page_title="Academic Burnout Detection", page_icon="📚")

# Title
st.title("📚 Academic Burnout Detection System")

# Sidebar
show_sidebar()

# Student Name
name = st.text_input("Enter Student Name")

st.subheader("Enter Student Details")

study_hours = st.slider("Study Hours per day", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)

assignment_load = st.slider("Assignment Load (1-10)", 1, 10, 5)
# screen_time = st.slider("Screen Time (hours)", 0, 12, 4)

# Prediction
if st.button("Predict Burnout"):

    prediction = predict_burnout(
        study_hours,
        sleep_hours,
        stress_level
    )

    # Result Display
    st.subheader(f"Result for {name if name else 'Student'}")

    if prediction == 0:
        st.success("Low Burnout 😊")
    elif prediction == 1:
        st.warning("Burnout level-Moderate Burnout ⚠️")
    else:
        st.error("High Burnout 🚨")

    # Burnout Score
    burnout_score = (stress_level * 10) - (sleep_hours * 2) + (study_hours * 2)
    burnout_score = max(0, min(100, burnout_score))

    st.subheader("Burnout Score")
    st.progress(burnout_score / 100)
    st.metric("Burnout Score", f"{burnout_score}%")

    # Chart Visualization
    data = pd.DataFrame({
        "Category": [
            "Study Hours",
            "Sleep Hours",
            "Stress Level",
            "Assignments",
            # "Screen Time"
        ],
        "Value": [
            study_hours,
            sleep_hours,
            stress_level,
            assignment_load,
            screen_time
        ]
    })

    st.subheader("Student Activity Overview")
    st.bar_chart(data.set_index("Category"))

    # Suggestions
    show_suggestions(prediction)

    # Download Report
    report = f"""
Academic Burnout Report

Student Name: {name}

Study Hours: {study_hours}
Sleep Hours: {sleep_hours}
Stress Level: {stress_level}

Burnout Score: {burnout_score}%
Prediction Level: {prediction}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="burnout_report.txt"
    )

st.markdown("---")
st.write("Developed using Streamlit | Academic Burnout Detection System")