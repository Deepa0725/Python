# Simple Interest Formula:

'''Simple Interest = ( P x R x T ) / 100
Where,
P is the principal amount
R is the rate of interest and
T is the time (number of years)'''


'''# 1. Write a Python program to calculate the simple interest
'''
# Python program to calculate simple interest

# store the inputs
P = float(input('Enter principal amount: '))
R = float(input('Enter the interest rate: '))
T = float(input('Enter time: '))

# calculate simple interest
SI = (P * R * T) / 100

# display result
print('Simple interest = ',SI )
print('Total amount = ',( P + SI ))

