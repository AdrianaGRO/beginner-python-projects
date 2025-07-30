"""
Project Name: Temperature Converter with History

Description:
Build a temperature conversion program that can convert between Celsius, Fahrenheit, and Kelvin. 
The program should use functions for each conversion type and store them in a dictionary, 
allowing users to select conversions by entering abbreviations ("c_to_f", "f_to_c", "c_to_k", etc.). 
The program should maintain a history of conversions and allow users to repeat conversions or clear history.

Key Concepts:
- Functions with return values (outputs)
- Storing functions as dictionary values
- Function composition and chaining
- Working with floating-point precision
- Managing program state (conversion history)

Example (Function as Dictionary Value):
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

conversions = {
    "c_to_f": celsius_to_fahrenheit
}

result = conversions["c_to_f"](25)  # Will return 77.0

Task Instructions:
- Write six conversion functions: celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, 
  kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
- Each function should take one temperature value and return the converted temperature
- Store these functions in a dictionary with keys: "c_to_f", "f_to_c", "c_to_k", "k_to_c", "f_to_k", "k_to_f"
- Use the dictionary to perform conversions based on user selection
- Demonstrate converting 100°C to Fahrenheit using the dictionary
- Maintain a list of conversion history (storing original temp, conversion type, and result)
- Implement functionality to display conversion history and clear it

Functionality:
1. Display available conversion options to the user
2. Ask the user to select a conversion type (e.g., "c_to_f")
3. Ask the user to enter the temperature value
4. Perform the conversion using the dictionary lookup
5. Display the result with proper formatting (1 decimal place)
6. Add the conversion to history (format: "25.0°C → 77.0°F")
7. Ask if the user wants to: perform another conversion, view history, clear history, or quit
8. Handle the user's choice and repeat as needed

Expected Output Format:
=== Temperature Converter ===
Available conversions: c_to_f, f_to_c, c_to_k, k_to_c, f_to_k, k_to_f

Conversion: c_to_f
Temperature: 25
Result: 25.0°C = 77.0°F

History (2 conversions):
1. 25.0°C → 77.0°F
2. 32.0°F → 0.0°C

Sample Function Calls and Expected Results:
celsius_to_fahrenheit(0) → 32.0
fahrenheit_to_celsius(212) → 100.0
celsius_to_kelvin(0) → 273.15
kelvin_to_celsius(273.15) → 0.0
fahrenheit_to_kelvin(32) → 273.15
kelvin_to_fahrenheit(273.15) → 32.0

conversions["c_to_f"](100) → 212.0

Hints:
- Celsius to Fahrenheit: (C × 9/5) + 32
- Fahrenheit to Celsius: (F - 32) × 5/9
- Celsius to Kelvin: C + 273.15
- Kelvin to Celsius: K - 273.15
- Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15
- Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32
- Use round() or format to display temperatures to 1 decimal place
- Store history as a list of formatted strings

TO DO List:
1. Write all six temperature conversion functions
2. Create a dictionary mapping conversion codes to functions
3. Test dictionary lookup with sample conversion (100°C to Fahrenheit)
4. Implement history tracking system (list to store conversion records)
5. Create function to display conversion history in numbered format
6. Create function to clear conversion history
7. Implement main program loop with user choices (convert, view history, clear history, quit)
8. Add proper formatting for temperature display (1 decimal place with units)
9. Test all conversions and history functionality with hard-coded values
10. Ensure no input() or print() statements in the solution file - use hard-coded test values only

Testing Requirements:
- Test each conversion function individually with known values
- Test dictionary lookup functionality
- Test history adding, viewing, and clearing
- Test the main program flow with various user choices
- All testing should use hard-coded values, not user input
"""


#1. Write all six temperature conversion functions

def celsius_to_fahrenheit(temperature):
    return f"{round(temperature * 9 / 5 + 32)}°F"


def fahrenheit_to_celsius(temperature):
    return f"{round((temperature - 32) * 5 / 9)}°C"


def celsius_to_kelvin(temperature):
    return f"{round(temperature + 273.15)}°K"


def kelvin_to_celsius(temperature):
    return f"{round(temperature - 273.15)}°C"


def fahrenheit_to_kelvin(temperature):
    return f"{round((temperature - 32) * 5/9 + 273.15)}°K"


def kelvin_to_fahrenheit(temperature):
    return f"{round((temperature - 273.15) * 9 / 5 + 32)}°F"


# 2. Create a dictionary mapping conversion codes to functions
temperature_dictionary = {
    "c_to_f" : celsius_to_fahrenheit,
    "f_to_c" : fahrenheit_to_celsius,
    "c_to_k" : celsius_to_kelvin,
    "k_to_c" : kelvin_to_celsius,
    "f_to_k" : fahrenheit_to_kelvin,
    "k_to_f" : kelvin_to_fahrenheit
}

conversion_units = {
    "c_to_f" : ("°C", "°F"),
    "f_to_c" : ("°F", "°C"),
    "c_to_k" : ("°C", "°K"),
    "k_to_c" : ("°K", "°C"),
    "f_to_k" : ("°F", "°K"),
    "k_to_f" : ("°K", "°F")
}

history = []


def do_conversion():
    user_input = float(input("Enter the temperature value to convert:\n"))
    print("Available conversions:")
    for symbol in temperature_dictionary:
            print(symbol)
    selection_conversion = input("Select a conversion type:\n")
    result = temperature_dictionary[selection_conversion](user_input)
    print(f"Result {user_input} -> {result}")
    input_unit, output_unit = conversion_units[selection_conversion]
    history.append(f"{user_input:.1f}{input_unit} → {result}")
    choice = input("Do you want to try another conversion? Type 'yes' or 'no':\n")
    if choice == 'yes':
        do_conversion()
    else:
        print("\n" * 15)
        main_menu()

def main_menu():
    while True:
        menu = input("Select one of your choice:\n"
                     "1. Convert\n"
                     "2. View history\n"
                     "3. Clear history\n"
                     "4. Quit\n").lower()
        if menu == "1":
            do_conversion()
        elif menu == "2":
            if history:
                print(f"History ({len(history)} conversions)")
                for i, conversion in enumerate(history,1):
                    print(f"{i}.{conversion}")
            else:
                print("No conversions in history yet")

        elif menu == "3":
            history.clear()
            print("History cleared!")

        elif menu =="4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please type 1 / 2 / 3 or 4")

print("===Temperature converter ===")
main_menu()