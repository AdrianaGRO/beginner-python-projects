# 6. BMI Calculator
# Write a program to calculate Body Mass Index (BMI).
# Prompt the user for weight in kilograms and height in meters.
# Calculate BMI using: weight / (height ** 2).
# Display the BMI floored to the nearest whole number (no decimals).
# Print the data type of BMI before flooring.


print("Welcome to Body Mass Index")
weight = float(input("What is your weight? Please use the metric in kilograms "))
height = float(input("What is your height? Please use the metric in meters "))
bmi = weight/(height ** 2)
print(f"The data type for bmi before flooring is - {type(bmi)}")
print(f"Your BMI is {round(bmi)}")
