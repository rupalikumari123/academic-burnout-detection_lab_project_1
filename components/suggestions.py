# import streamlit as st

# def show_suggestions(level):

#     st.subheader("Suggestions")

#     if level == 0:
#         st.write("✅ Maintain your current study schedule")
#         st.write("✅ Continue healthy habits")

#     elif level == 1:
#         st.write("⚠️ Take short breaks while studying")
#         st.write("⚠️ Reduce screen time")
#         st.write("⚠️ Try meditation")

#     else:
#         st.write("🚨 High burnout detected")
#         st.write("• Take proper rest")
#         st.write("• Talk with mentors or teachers")
#         st.write("• Reduce workload temporarily")




import streamlit as st

def show_suggestions(level):

    st.subheader("Smart Suggestions")

    if level == 0:
        st.write("✅ Maintain your current routine")
        st.write("✅ Continue healthy sleep habits")
        st.write("✅ Balance study and recreation")

    elif level == 1:
        st.write("⚠️ Take regular study breaks")
        st.write("⚠️ Reduce screen time")
        st.write("⚠️ Practice meditation or exercise")
        st.write("⚠️ Improve sleep schedule")

    else:
        st.write("🚨 High burnout detected")
        st.write("• Take adequate rest")
        st.write("• Reduce workload temporarily")
        st.write("• Talk with mentors or counselors")
        st.write("• Maintain physical activity")