# ===== DAY 2: Variables and Built-in Functions =====
# This script demonstrates variable declaration, data types, and built-in functions

import math  # Import math module for mathematical operations

# ===== Section 1: Variable Declaration and Initialization =====
firstname = None  # Initialize as None, will be filled with user input later
lastname = None   # Initialize as None
fullname = 'pius john'  # String variable
country = None    # Initialize as None
city = 'otukpo'   # String variable with city name
age = 21          # Integer variable
year = 2026       # Integer variable for current year
is_married = False  # Boolean variable (False means not married)
is_true = True    # Boolean variable set to True
is_light_on = True  # Boolean variable representing a light state
school, dreamcity, = "Miva Open University", "Germany"  # Multiple variable assignment (tuple unpacking)

# ===== Section 2: Explore Data Types with type() Function =====
print(type(city))  # Check and display the type of 'city' variable (should be <class 'str'>)
print(type(is_married))  # Check and display the type of 'is_married' variable (should be <class 'bool'>)
# print(len(firstname))  # Commented out: would cause error as firstname is None

# ===== Section 3: Circle Calculations using math Module =====
radius = None  # Initialize radius variable
print("Enter radius of circle")
radius = float(input())  # Get radius from user and convert to float

# Calculate circle's area using formula: A = πr²
area_of_circle = math.pi * (radius ** 2)
# Calculate circle's circumference using formula: C = 2πr
circum_of_circle = 2 * math.pi * radius

# Display the calculated area and circumference
print("Area: ", area_of_circle)
print("Circumference: ", circum_of_circle)

# ===== Section 4: User Input and String Formatting =====
# Prompt user to enter personal information
print("Enter your firstname: ")
firstname = input()  # Get firstname from user input

print("Enter your lastname: ")
lastname = input()  # Get lastname from user input

print("Enter your country: ")
country = input()  # Get country from user input

# Display personalized welcome message using f-string formatting
print(f"Welcome {firstname} {lastname}, from {country}")