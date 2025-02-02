'''1. Write a Python program to add two numbers.'''
# python program to add two numbers

# take inputs
num1 = 5
num2 = 10

# add two numbers
sum = num1 + num2

# displaying the addition result
print('{0} + {1} = {2}'.format(num1, num2, sum))


'''2. write a python program to accept two number from user, add the numbers and display it?'''
# python program to add two numbers with user input

# store input numbers
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

# add two numbers
# User might also enter float numbers
sum = float(num1) + float(num2)

# displaying the adding result
# value will print in float
print('The sum of numbers {0} and {1} is {2}'.format(num1, num2, sum))


'''3. write a program to add two numbers using function in python'''
# Python program to add two numbers using function

def add_num(a,b):   #user-defined function
    sum = a + b   #adding numbers
    return sum   #return value

# take input
num1 = float(input('Enter first number : '))
num2 = float(input('Enter second number : '))

# function call
print('The sum of numbers {0} and {1} is {2}'
       .format(num1, num2, add_num(num1, num2)))


'''#4.  Python program to subtract two numbers
'''
# take inputs
num1 = 10
num2 = 7

# subtract two numbers
sub = num1 - num2

# print the subtraction result
print('The subtraction of numbers =', sub)


'''#5. Python program to subtract two numbers
'''
# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# subtract two numbers
sub = num1 - num2

# print the subtraction result
# value will print in float
print('The subtraction of numbers = %0.2f' %sub)


'''# 6. Python program to subtract two numbers
'''
def sub_num(num1, num2):  #user-defined function
    #subtract two numbers
    return num1-num2
    
# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calling function and print the subtraction value
print('The subtraction of numbers = %0.2f' %sub_num(num1, num2))


'''7. Write a Python program to accept two numbers multiply them and print the result
'''
# Python program to multiply two number

# take inputs
num1 = 3
num2 = 5

# calculate product
product = num1*num2

# print multiplication value
print("The Product of Number:", product)


'''8. Write a Python program to ask from the user two numbers and print their product
'''
# Python program to multiply two number

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calculate product
product = num1*num2

# print multiplication value
print("The Product of Number: %0.2f" %product)


'''#9.  Python program to multiply two numbers using function
'''
def product_num(num1, num2):  #user-defind function
    num = (num1 * num2)   #calculate product
    return num   #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# function call
product = product_num(num1, num2)

# print multiplication value
print("The Product of Number: %0.2f" %product)


'''10. Write a python program to find division between two numbers
'''
# Python program to divide two numbers

# take inputs
num1 = 10
num2 = 2

# Divide numbers
division = num1/num2

# print value
print("The division of {0} and {1} is {2}"
               .format(num1,num2,division))


'''11. Write a program to perform division using variables in python
'''
# Python program to divide two numbers

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Divide numbers
division = num1/num2

# print value
print("The division of {0} and {1} is {2}"
                .format(num1,num2,division))


'''#12.  Python program to divide two numbers using function
'''
def div_Num(num1, num2):  #user-defined function
    div = (num1/num2)   #divide numbers
    return div   #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# function call
division = div_Num(num1, num2)

# print value
print("The division of {0} and {1} is {2}"
                .format(num1,num2,division))


'''#13. Python program to find average of two numbers
'''
# first number
num1 = 10
# second number
num2 = 20

# calculate average of those numbers
avg = (num1 + num2) / 2

# print average value
print('The average of numbers = %0.2f' %avg)


'''#14. Python program to find average of two numbers
'''
# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calculate average of those numbers
avg = (num1 + num2) / 2

# print average value
print('The average of numbers = %0.2f' %avg)


'''#15.  Python program to find average of two numbers using function
'''
def avg_num(num1, num2):   #user-defined function
    avg = (num1 + num2) / 2   #calculate average
    return avg    #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# function call
average = avg_num(num1, num2)

# display result
print('The average of numbers = %0.2f' %average)

#  Output: 
# Enter first number: 25
# Enter second number: 48
# The average of numbers = 36.50


'''16. Print the Square of a Number in Python Using Simple Multiplication
'''
a = 3
square = a * a
print(square)   #Output:-9


'''17. Same Program by defining a function
'''
def square(a):
    return a*a

print(square(5))       # Output:25


'''#18.  Python program to swap two variables using temporary variable
'''
# take inputs
a = input('Enter the value of a: ')
b = input('Enter the value of b: ')

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# create a temporary variable and swap the value
temp = a
a = b
b = temp

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)

# Output:-

'''Enter the value of a: 10
Enter the value of b: 20
Values Before Swapping
a = 10 and b = 20
Values After Swapping
a = 20 and b = 10'''


'''#19.  Python program to swap two numbers 
# without using temporary variable'''

# take inputs
a = input('Enter the value of a: ')
b = input('Enter the value of b: ')

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swap the value
a, b = b, a

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)

# Output:-

'''Enter the value of a: 5.5
Enter the value of b: 7
Values Before Swapping
a = 5.5 and b = 7
Values After Swapping
a = 7 and b = 5.5'''


'''#20.  Python program to swap two numbers using + and – operator
'''
# take inputs
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = a + b
b = a - b
a = a - b

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)

# Output:-

'''Enter the value of a: 15
Enter the value of b: 22
Values Before Swapping
a = 15.0 and b = 22.0
Values After Swapping
a = 22.0 and b = 15.0'''


'''#21 Python program to swap two numbers using * and / operator
'''
# take inputs
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = a * b
b = a / b
a = a / b

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)

# Output:-

'''Enter the value of a: 13.6
Enter the value of b: 10
Values Before Swapping
a = 13.6 and b = 10.0
Values After Swapping
a = 10.0 and b = 13.6'''