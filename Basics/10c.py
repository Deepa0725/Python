# Practice Programs

# 1.Basic Counting with while Loop:
'''Write a program that counts from 1 to 10 using a while loop.'''

i = 0

while i <= 10:
    print(i)
    i += 1
    
# OUTPUT:
'''
0
1
2
3
4
5
6
7
8
9
10
'''

# 2. Odd Numbers Printer:
'''Create a program that prints all odd numbers between 1 and 20 using a while loop.'''

i = 0
 
while i <= 20:
    if i%2 != 0:
        print(i)
    i += 1

# OUTPUT:
'''
1
3
5
7
9
11
13
15
17
19'''

#3. Ticket Booking Simulation:
'''Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked,
the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."'''

# Ticket Booking Simulation
seats = 8  # Total number of seats

while seats > 0:
    print(f"Seats available: {seats}")
    booking = input("Would you like to book a seat? (yes/no): ").strip().lower()
    
    if booking == "yes":
        seats -= 1
        print(f"Seat booked! {seats} seats remaining.")
    elif booking == "no":
        print("Booking cancelled.")
    else:
        print("Invalid input, please enter 'yes' or 'no'.")

print("All seats are booked.")

# OUTPUT:
'''
Seats available: 8
Would you like to book a seat? (yes/no): yes
Seat booked! 7 seats remaining.
Seats available: 7
Would you like to book a seat? (yes/no): yes
Seat booked! 6 seats remaining.
Seats available: 6
Would you like to book a seat? (yes/no): no
Booking cancelled.
Seats available: 6
Would you like to book a seat? (yes/no): yes
Seat booked! 5 seats remaining.
Seats available: 5
Would you like to book a seat? (yes/no): fdg
Invalid input, please enter 'yes' or 'no'.
Seats available: 5
Would you like to book a seat? (yes/no): yes
Seat booked! 4 seats remaining.
Seats available: 4
Would you like to book a seat? (yes/no): yes
Seat booked! 3 seats remaining.
Seats available: 3
Would you like to book a seat? (yes/no): yes
Seat booked! 2 seats remaining.
Seats available: 2
Would you like to book a seat? (yes/no): yes
Seat booked! 1 seats remaining.
Seats available: 1
Would you like to book a seat? (yes/no): yes
Seat booked! 0 seats remaining.
All seats are booked.'''

'''strip() removes any extra spaces the user might accidentally input.
lower() ensures the input is case-insensitive (e.g., "Yes", "YES", or "yes" will all work)'''

#4. Countdown Timer:
'''Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.'''

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1
    
print("HAPPY NEW YEAR")


