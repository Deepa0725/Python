# EXAMPLES
# 1 Basic Conditions:

'''# Write a program to check if someone is eligible for a bus pass. 
If they are below 5 years, the bus pass is free. 
If they are 60 years or older, they get a senior citizen discount.
Otherwise, they pay the full price.
'''
# program
person = input("Enter the person: ")
age = int(input("Enter the age: "))
    
if age < 5:
    print("Bus pass is free")
elif age > 60:
    print("Person gets a seinor citixen discount")
else:
    print("Person pay the full price")

#2 Meal Time Checker:

'''Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."'''

# program
time = int(input("Enter the time: "))

if time == 8:
    print("Its time for breakfast")
elif time == 13:
    print("Its time for lunch")
elif time == 20:
    print("Its time for Dinner")
else:
    print("Its not time for a meal")

#3 Simple Eligibility Check:

'''Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. 
If they are 60 or older, they get a senior citizen membership. 
Otherwise, they get a regular membership.'''

# program
age = int(input("Enter your Age: "))


if age < 18:
    print("Person gets a student membership")
elif age > 60:
    print("Person gets a senior citizenship")
else:
    print("Person gets a regular membership")
    
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
    
    
# 8. Indentation in Python
'''Python uses indentation (spaces at the beginning of a line) to define blocks of code. 
The indented code after an if, elif, or else statement belongs to that condition. 
Make sure to use consistent indentation to avoid errors.
'''
# Example1:
age = 19

if age >= 18:
    print("You are eligible to vote.")
    print("Remember to bring your voter ID.")
else:
    print("You are not eligible to vote.")
    
'''In the example above, the two print() statements are part of the if block because they are indented. 
Be careful to maintain the correct indentation for your code to run correctly.
'''

# Sets in Python
'''A set is a collection of unique items that is unordered and unindexed. Sets do not allow duplicate values. 
Sets are useful for performing operations like union, intersection, and difference.'''

# Syntax:
'''my_set = {element1, element2, element3, ...}'''


fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
print(fruits_set)
print(numbers_set)

s = {10, 200, 3}       # set is unordered  output:{200, 10, 3}
print(s)

# print(s[0])    Set is unindexed

s2 = set((1, 2, 3))        #Another form for declare sets
print(s2)
print(type(s2))


#1 Empty Set:
'''To create an empty set, use the set() function (not {}, which creates an empty dictionary).'''

empty_set = set()   
# s = {}   - it is dictionary not set


# 2. Set Operations
'''Sets support mathematical operations like union, intersection, and difference.'''

# Union:(OR)
'''The union of two sets combines all elements from both sets, removing duplicates.'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
print(union_set)

# Intersection:(AND)
'''The intersection of two sets returns elements that are common to both sets.'''

intersection_set = set1 & set2  # Output: {3}
print(intersection_set)

# Difference:
'''The difference between two sets returns elements that are in the first set but not in the second.'''

difference_set = set1 - set2  # Output: {1, 2}
print(difference_set)

# Symmetric Difference:
'''The symmetric difference returns elements that are in either of the sets but not in both.'''

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
print(sym_diff_set)


#3. Set Methods
'''Sets come with several useful methods for performing common tasks.'''

# add(): Adds an element to the set.
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}


# remove(): Removes a specified element from the set. Raises an error if the element does not exist.
fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple','orange', 'cherry'}

'''fruits_set.remove("Mango")
print(fruits_set)      #keyerror:mango
'''
# discard(): Removes a specified element without raising an error if it does not exist.
fruits_set.discard("banana")  # No error if "banana" is not in the set
print(fruits_set)

# pop(): Removes a random element from the set.
fruits_set.pop()
print(fruits_set)


# clear(): Removes all elements from the set.
fruits_set.clear()
print(fruits_set)


# 9. Differences Between Lists, Tuples, and Sets
'''Feature	  List	                Tuple	            Set
Ordering	  Ordered	            Ordered	            Unordered
Mutability	  Mutable	            Immutable	        Mutable
Duplicates	  Allows duplicates	    Allows duplicates	No duplicates
Indexing	  Supports indexing	    Supports indexing	No indexing
Operations	  List operations	    Tuple operations	Set operations
Common Uses	  General collection	Fixed data	        Unique items'''