import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️❤" 
)

# Title
st.title("⚖️❤ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

# Input fields
weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=70.0
)

height = st.number_input(
    "Enter your height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

# Calculate button
if st.button("Calculate BMI"):

    # Convert height from cm to meters
    height_m = height / 100

    # BMI calculation
    bmi = weight / (height_m ** 2)

    # Display BMI
    st.subheader(f"Your BMI is: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")