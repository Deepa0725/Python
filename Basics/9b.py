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

