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