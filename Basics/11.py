# For Loops in Python

'''In Python, a for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code repeatedly 
for each element in the sequence.'''

# 1. The Basic Structure of a for Loop
'''A for loop allows you to repeat a block of code a fixed number of times, or once for each element in a sequence.
'''

# Syntax:
'''for item in sequence:
'''    # Code to execute for each item in the sequence
    
    
# Example1:
'''Let’s print each name in a list of Kannada cities:
'''
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
    
# Output:
'''
Bengaluru
Mysuru
Hubballi
Mangaluru
'''
# Example2:

bag =["Red", "Green", "Blue"]
for ball in bag:
    print(ball)

# 2. Using range() with for Loops
'''The range() function generates a sequence of numbers, which you can use in a for loop when you want to repeat a block of code 
a specific number of times.'''

# Syntax of range():
'''range(start, stop, step)
'''

# start: The starting value (inclusive).
# stop: The ending value (exclusive).
# step: The increment (optional, default is 1).


# Example1 : Counting from 1 to 10
for i in range(1, 11):
    print(i)
'''This loop will print the numbers from 1 to 10.
'''
# Output:
'''
1
2
3
4
5
6
7
8
9
10'''

# Example2: Same above program using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# output:
'''
1
2
3
4
5
6
7
8
9
10'''


# Example3: Counting by 2s from 1 to 10

for i in range(1, 11, 2):
    print(i)
    
'''This loop prints only the odd numbers between 1 and 10.
'''
# Output:
'''
1
3
5
7
9'''


# 3. Looping Over Strings
'''You can also loop over each character in a string using a for loop.
'''
# Example1 : Printing each character in a string

name = "Karnataka"
for letter in name:
    print(letter)
    
# Output:
'''    
K
a
r
n
a
t
a
k
a'''

'''This loop goes through the string "Karnataka" one character at a time.'''

# Example2

name = " DEEPA"

for letter in name:
    print(letter)
    
# Output:
'''
D
E
E
P
A'''

# Example3:       ENUMERATE

name = " DEEPA"

for index, letter in enumerate(name):
    print(letter*(index + 0))


