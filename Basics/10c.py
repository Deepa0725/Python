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

