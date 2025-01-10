# Conditional Statements in Python: if, elif, and else
# In programming, conditional statements are used to perform different actions based on different conditions. Python uses if, elif, and else statements to allow your program to make decisions.

# 1. The if Statement
# The if statement is used to test a condition. If the condition is True, the block of code under the if statement is executed.

Syntax:
if condition:
    # Code block to execute if the condition is True
# Example:
# Let's say you want to check if it's time for dinner (assuming dinner time is 8 PM).

time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
# Here, the program checks if the variable time is equal to 20 (8 PM). If it's 20, the message "It's time for dinner!" is printed.

# 2. The else Statement
# The else statement provides an alternative block of code to execute when the if condition is False.

Syntax:
if condition:
    # Code block if the condition is True
else:
    # Code block if the condition is False
Example:
Let's extend the dinner example by adding an alternative action if it's not 8 PM.

time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")
If the condition (time == 20) is False (because the time is 6 PM), the program prints "It's not dinner time yet."

3. The elif Statement
The elif (short for "else if") statement checks another condition if the previous if or elif condition was False. You can have multiple elif statements to test various conditions.

Syntax:
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if none of the above conditions are True
Example:
Let’s create a system to check meal times based on the time of the day:

time = 15  # 3 PM

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")
# Here, the program checks multiple conditions:

# If the time is 8 AM, it prints "It's breakfast time!".
# If the time is 1 PM, it prints "It's lunch time!".
# If the time is 8 PM, it prints "It's dinner time!".
# If none of these conditions are true, it prints "It's not a meal time."
# 4. Comparison Operators in if Statements
# You can use comparison operators to compare values in if statements:

==: Equal to
!=: Not equal to
<: Less than
>: Greater than
<=: Less than or equal to
>=: Greater than or equal to
Example:
Let’s check if someone is eligible to vote in Karnataka (minimum age for voting is 18).

age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
Here, the condition age >= 18 checks if the age is greater than or equal to 18. If True, it prints that the person is eligible to vote. Otherwise, it prints that they are not eligible.

5. Logical Operators in if Statements
You can also use logical operators to combine multiple conditions in if statements:

and: Returns True if both conditions are True
or: Returns True if at least one condition is True
not: Reverses the result of a condition
Example:
Let’s say you want to check if someone is eligible for a student discount. The person must be both under 18 years of age and have a student ID.

age = 16
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")
Here, the condition age < 18 and has_student_id checks if both conditions are True. If so, the message "You are eligible for the student discount!" is printed.

6. Example: Checking Bus Ticket Prices
Let’s create an example based on ticket prices for a Karnataka KSRTC bus. If the passenger is under 5 years old, the ticket is free. If the passenger is between 5 and 12 years old, they get a child discount. If the passenger is 60 years or older, they get a senior citizen discount. Otherwise, they pay the full fare.

age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")
In this example:

If the passenger is younger than 5 years, the output is "Ticket is free."
If they are 5 to 12 years old, it prints "You get a child discount."
If they are 60 or older, it prints "You get a senior citizen discount."
For all other ages, it prints "You pay the full fare."
7. Nested if Statements
You can also use if statements inside other if statements. This is called nesting.

Example:
Let’s say you’re planning to visit Mysuru. You want to decide whether to go based on the day of the week and the weather.

day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")
Here, the program first checks if it’s a weekend. If it is, it checks the weather. If it’s not raining, it prints "Let's visit Mysuru!", otherwise, it prints "It's raining, let's stay home." On weekdays, it prints "It's a weekday, let's wait for the weekend."

8. Indentation in Python
Python uses indentation (spaces at the beginning of a line) to define blocks of code. The indented code after an if, elif, or else statement belongs to that condition. Make sure to use consistent indentation to avoid errors.

Example:
age = 19

if age >= 18:
    print("You are eligible to vote.")
    print("Remember to bring your voter ID.")
else:
    print("You are not eligible to vote.")
In the example above, the two print() statements are part of the if block because they are indented. Be careful to maintain the correct indentation for your code to run correctly.

Homework
Basic Conditions:

Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
Meal Time Checker:

Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."
Simple Eligibility Check:

Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.

While Loops in Python
A loop is a programming structure that repeats a set of instructions as long as a specified condition is True. In Python, the while loop allows you to repeatedly execute a block of code as long as the condition is True.

1. The Basic Structure of a while Loop
The while loop repeatedly executes a block of code as long as the condition is True.

Syntax:
while condition:
    # Code to execute as long as condition is True
Example:
Let’s print numbers from 1 to 5 using a while loop.



i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing i by 1 after each iteration
    
    i = 1
while i <= 5:
    print(i)
    # Forgot to update i, so the condition remains True forever!
    
    
    Sheep 1
Sheep 2
Sheep 3
Sheep 4
Sheep 5
That's enough counting!


Sheep 1
Sheep 2
Sheep 3
Sheep 5

sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1
    
    pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")

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