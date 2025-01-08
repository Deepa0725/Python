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

# Output for the different input values:-

'''Enter principal amount: 1000
Enter the interest rate: 5
Enter time: 10
Simple interest = 500.0
Total amount = 1500.0

Enter principal amount: 7000
Enter the interest rate: 7.5
Enter time: 5
Simple interest = 2625.0
Total amount = 9625.0

Enter principal amount: 25000
Enter the interest rate: 3.8
Enter time: 7.4
Simple interest = 7030.0
Total amount = 32030.0'''