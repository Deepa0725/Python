# 7. Real-life Example: KSRTC Bus Seats Availability
'''Let’s say you want to simulate a KSRTC bus seat booking system. The bus has 5 available seats. 
Each time a seat is booked, the available seats decrease.
'''
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

'''Here, the loop keeps running until all seats are booked. It checks the available seats and asks the user if they want to book one. The loop stops when there are no more seats available.
'''
# Output Example:

'''
5 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
4 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
...
1 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
All seats are booked!'''


# 8. Nested while Loops
'''You can also nest while loops inside each other. This can be useful in more complex scenarios, such as checking multiple 
conditions or dealing with multi-level data.'''

# Example:
'''Let’s simulate a snack machine that allows users to buy snacks as long as both the machine has snacks and the user has money:
'''

snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()
    
    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        
print("Either snacks are sold out or you are out of money.")

'''This loop will continue as long as there are snacks available and the user has money. 
Once one condition is no longer True, the loop stops.'''

# output:
'''
Snacks available: 3. Money: ₹10
Do you want to buy a snack for ₹5? (yes/no): yes
Snack purchased!
Snacks available: 2. Money: ₹5
Do you want to buy a snack for ₹5? (yes/no): yes
Snack purchased!
Either snacks are sold out or you are out of money.'''