# 8. Travel Distance Estimator
# Develop a program to estimate travel time.
# Ask the user for distance in kilometers and speed in kilometers per hour.
# Calculate the time taken as distance divided by speed.
# Display the time rounded to 2 decimal places.
# Print the data type of the time.

print("Welcome to Travel Distance Estimator")
distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the speed in kilometers/hour: "))
time = distance / speed
print(f"The time for the distance of {distance:.0f} km and with a speed of {speed:.0f} km/h the estimated time is {time:.2f} hours")
print(f"The data type for time is: {type(time)}")