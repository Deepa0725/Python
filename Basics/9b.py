# EXAMPLES
# 1 Basic Conditions:

'''# Write a program to check if someone is eligible for a bus pass. 
If they are below 5 years, the bus pass is free. 
If they are 60 years or older, they get a senior citizen discount.
Otherwise, they pay the full price.
'''
# program
person = input("Enter the person: ")
age = int(input("Enter the age: "))
    
if age < 5:
    print("Bus pass is free")
elif age > 60:
    print("Person gets a seinor citixen discount")
else:
    print("Person pay the full price")

#2 Meal Time Checker:

'''Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."'''

# program
time = int(input("Enter the time: "))

if time == 8:
    print("Its time for breakfast")
elif time == 13:
    print("Its time for lunch")
elif time == 20:
    print("Its time for Dinner")
else:
    print("Its not time for a meal")

