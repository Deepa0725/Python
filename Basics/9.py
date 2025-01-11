# Conditional Statements in Python: if, elif, and else
'''In programming, conditional statements are used to perform different actions based on different conditions. 
Python uses if, elif, and else statements to allow your program to make decisions.'''

# 1. The if Statement
'''The if statement is used to test a condition. If the condition is True, the block of code under the if statement is executed.'''

# Syntax:
'''if condition:
'''    # Code block to execute if the condition is True


# Example1:
'''Let's say we want to check if it's time for dinner (assuming dinner time is 8 PM).
'''

time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
    
# Example2:
x = 26
if x==26:
    print("Yes x is 26")

# Example3:
x = 29
if x==26:
    print("Yes x is 26")   #Prints nothing
    
# Example4:
y = 4
if (y%2) == 0 :
    print("Number is even")   

# Example5:
y = 5
if (y%2) != 0 :
    print("Number is 0dd")    

 
# 2. The else Statement
'''The else statement provides an alternative block of code to execute when the if condition is False.
'''

# Syntax:
'''if condition:
    # Code block if the condition is True
else:
    # Code block if the condition is False'''
    
    
# Example1:
'''Let's extend the dinner example by adding an alternative action if it's not 8 PM.
'''
time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")

    
# Example2:
y = 9
if (y%2) == 0 :
    print("Number is even") 
else:
    print("Number is Odd") 
    
# Example3:
signal = 'red'

if signal=="red":
    print("STOP")
else:
    print("GO")
    
    # 3. The elif Statement
'''The elif (short for "else if") statement checks another condition if the previous if or elif condition was False. You can have multiple elif statements to test various conditions.
'''
# Syntax:
'''if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if none of the above conditions are True'''
    
 # Example1:
time = 15  # 3 PM

if time == 8:
    print("It's breakfast time!")            #If the time is 8 AM, it prints "It's breakfast time!"
elif time == 13:
    print("It's lunch time!")                #If the time is 1 PM, it prints "It's lunch time!".
elif time == 20:
    print("It's dinner time!")               #If the time is 8 PM, it prints "It's dinner time!".
else:
    print("It's not a meal time.")           #If none of these conditions are true, it prints "It's not a meal time."
    
    # Example2:
signal = "green"

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
else:
    print("GO")
    
     # Example3:
signal = input("Enter the signal color: ")

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
elif signal == "green":
    print("GO")
else:
    print("Nothing")
    
    
# 4. Comparison Operators in if Statements
'''==: Equal to
!=: Not equal to
<: Less than
>: Greater than
<=: Less than or equal to
>=: Greater than or equal to'''

# Example1:
'''Let’s check if someone is eligible to vote in Karnataka (minimum age for voting is 18).
'''
age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 5. Logical Operators in if Statements

'''and: Returns True if both conditions are True
or: Returns True if at least one condition is True
not: Reverses the result of a condition'''

# Example1:
'''Let’s say you want to check if someone is eligible for a student discount. The person must be both under 18 years of age 
and have a student ID.'''


age = 16
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")
    
# Example2:
att = 65
is_teacher_friend = True

if att >= 75 or is_teacher_friend == True:
    print("EXAM")
else:
    print("NO EXAM")
    
    # Example3:
att = 65
is_teacher_friend = True

if att >= 75 and is_teacher_friend == True:
    print("EXAM")
else:
    print("NO EXAM")


# 6. Example1: Checking Bus Ticket Prices
'''Let’s create an example based on ticket prices for a Karnataka KSRTC bus. 
If the passenger is under 5 years old, the ticket is free. 
If the passenger is between 5 and 12 years old, they get a child discount. 
If the passenger is 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full fare.'''

age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")


# 7. Nested if Statements
'''You can also use if statements inside other if statements. This is called nesting.
'''
# Example1:
'''Let’s say you’re planning to visit Mysuru. You want to decide whether to go based on the day of the week and the weather.
'''
day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")
    
'''Here, the program first checks if it’s a weekend. If it is, it checks the weather. 
If it’s not raining, it prints "Let's visit Mysuru!", 
otherwise, it prints "It's raining, let's stay home." 
On weekdays, it prints "It's a weekday, let's wait for the weekend."'''


# Example2:

gender = input("Enter the sex: ")
age = int(input("Enter the age: "))

if gender == "female":
    print("Ticket is Free")
    
else:
    if age < 5:
        print("Ticket is free.")
    elif age <= 12:
        print("You get a child discount.")
    elif age >= 60:
        print("You get a senior citizen discount.")
    else:
        print("You pay the full fare.")
    
    

