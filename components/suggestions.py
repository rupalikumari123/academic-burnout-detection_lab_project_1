import streamlit as st

def show_suggestions(level):

    st.subheader("Smart Suggestions")

    if level == 0:
        st.write("✅ Maintain current routine")
        st.write("✅ Keep balanced study schedule")

    elif level == 1:
        st.write("⚠️ Take regular breaks")
        st.write("⚠️ Improve sleep habits")
        st.write("⚠️ Reduce workload slightly")

    else:
        st.write("🚨 High burnout detected")
        st.write("• Take proper rest")
        st.write("• Reduce academic pressure")
        st.write("• Talk with mentors")
        st.write("• Practice physical activity")