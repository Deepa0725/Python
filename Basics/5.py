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