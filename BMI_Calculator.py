import streamlit as st

def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight / (height^2)
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Set title
    st.title("BMI Calculator")
    
    # Input weight in kilograms
    weight_kg = st.number_input("Enter your weight in kilograms", min_value=0.0)
    
    # Input height in meters
    height_m = st.number_input("Enter your height in meters", min_value=0.0)
    
    if st.button("Calculate BMI"):
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_m)
        
        # Interpret BMI
        bmi_category = interpret_bmi(bmi)
        
        # Display BMI and category
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"You are {bmi_category}.")

if __name__ == "__main__":
    main()

