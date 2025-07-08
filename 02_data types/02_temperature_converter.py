# 2. Temperature Converter
# Write a program that converts a temperature from Celsius to Fahrenheit.
# Prompt the user to enter a temperature in Celsius.
# Use the formula: Fahrenheit = (Celsius * 9/5) + 32.
# Display the Fahrenheit temperature rounded to 1 decimal place using an f-string.
# Print the data type of the Fahrenheit value.

print("Temperature Converter from Celsius to Fahrenheit")
print("----------------------")
celsius = float(input("Enter the temperature in Celsius: \n"))
fahrenheit = round((celsius * 9/5) + 32 , 1)
print(f"Your temperature in Fahrenheit is: {fahrenheit}")
print(type(fahrenheit))