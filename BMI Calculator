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
    # Input weight in kilograms
    weight_kg = float(input("Enter your weight in kilograms: "))
    
    # Input height in meters
    height_m = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)
    
    # Interpret BMI
    bmi_category = interpret_bmi(bmi)
    
    # Display BMI and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are {bmi_category}.")

if __name__ == "__main__":
    main(
