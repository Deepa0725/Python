# For Loops in Python
'''In Python, a for loop is used to iterate over a sequence (like a list, tuple, string, or range) and 
execute a block of code repeatedly for each element in the sequence.'''

# 1. The Basic Structure of a for Loop
'''A for loop allows you to repeat a block of code a fixed number of times, or once for each element in a sequence.
'''

# Syntax:
'''for item in sequence:
'''    # Code to execute for each item in the sequence

# Example1:

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
    
# Output:
'''Bengaluru
Mysuru
Hubballi
Mangaluru'''


# 2. Using range() with for Loops
'''The range() function generates a sequence of numbers, which you can use in a for loop 
when you want to repeat a block of code a specific number of times.
'''
# Syntax of range():