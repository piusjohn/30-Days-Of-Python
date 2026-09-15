import math
#Day 2: 30 Days of python programming

firstname = None
lastname = None
fullname = 'pius john'
country = None
city = 'otukpo'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
school, dreamcity, = "Miva Open University", "Germany"

print(type(city))
print(type(is_married))
#print(len(firstname))

radius = None
print ("enter radius of circle")
radius = float(input())

area_of_circle = math.pi * (radius **2)
circum_of_circle = 2 * math.pi * radius
print("Area: ",area_of_circle)
print("circumference ", circum_of_circle)

print("Enter your firstname: ")
firstname = input()
print("Enter your lastname: ")
lastname = input()
print("Enter your country: ")
country = input()

print(f"welcome {firstname} {lastname}, from {country}")