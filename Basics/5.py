# None datatype
x = None
print(type(x))

#Operators

# Assignment Operators
x = 5  # Assigns 5 to x
print(x)

x += 3  # Equivalent to x = x + 3, now x is 8
print(x)

x -= 2  # Equivalent to x = x - 2, now x is 6
print(x)

x *= 4  # Equivalent to x = x * 4, now x is 24
print(x)

x /= 6  # Equivalent to x = x / 6, now x is 4.0
print(x)

# Comparison Operators
a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25)  # Output: True

#  Logical Operators
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not(True))
print(not(False))

x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True)

# or operator
print(x > 10 or z > 10)  # Output: True (one of the conditions is True)

# not operator
print(not(x > 10))  # Output: True (reverses False to True)


# Membership Operators
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list)  # Output: True (3 is in the list)
print(6 not in my_list)  # Output: True (6 is not in the list)
print("P" in my_string)  # Output: True ("P" is in the string)
print("z" not in my_string)  # Output: True ("z" is not in the string)

string = "Deepa"
print("D" in string)
print("D" not in string)
print("S" not in string)

string1 = "Deepag"
print("D" in string) and ("D" in string)
print("D" in string) or ("D" in string)
print("D" not in string) and ("D"  not in string)


# Bitwise Operators
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)

# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)

# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)

# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)

# Left shift
print(a << 1)  # Output: 10 (binary: 1010)

# Right shift
print(a >> 1)  # Output: 2 (binary: 010)

# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)

#1  LOGICAL OPERATORS Write a Python program that takes two numbers as input from the user and checks if:
num1 = int(input("Enter a number:" ))
num2 = int(input("Enter a number:" ))

# Both numbers are greater than 10 (using and).
print(num1 > 10 and num2 > 10)

# At least one of the numbers is less than 5 (using or).
print(num1 < 5 or num2 < 5)

# The first number is not greater than the second (using not).
print(not(num1 < num2))


#2 COMPARISION OPERATOR a Python program that asks the user for their age and prints:
''' "You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.'''

age = int(input("Enter your Age: "))
if age >= 18:
    print("You are a Adult")
elif age < 18:
    print("You are a minor")
    
    
# 3 Membership Operator : Write a Python program that:
'''Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in)'''

xyz = input("Enter the string: ")
print("a" in xyz)
print("Python" not in xyz)


# Bitwise Operator : Given two integers, write a Python program that:
'''Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1)'''

h = int(input("Enter a number1: "))
j = int(input("Enter a number2: "))
print(h & j)
print(h | j)
print(h ^ j)
print(h << 2)
print(j >> 1)