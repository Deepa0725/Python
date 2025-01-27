# While Loops in Python
'''A loop is a programming structure that repeats a set of instructions as long as a specified condition is True. 
In Python, the while loop allows you to repeatedly execute a block of code as long as the condition is True.'''


# 1. The Basic Structure of a while Loop
'''The while loop repeatedly executes a block of code as long as the condition is True.
'''
# Syntax:
'''while condition:    '''           # Code to execute as long as condition is True

# Example1:
# Let’s print numbers from 1 to 5 using a while loop.

i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing i by 1 after each iteration
    
'''The loop starts with i = 1 and checks if i <= 5.
As long as this condition is True, it prints the value of i and increases it by 1 (i += 1).
The loop ends when i becomes 6, as the condition i <= 5 becomes False.'''

# Output:
'''
1
2
3
4
5'''

#Example2
'''condition = True

while condition:
    print("Condition is true")'''         #Gives stm continously
    
# Example3
is_failed = True
i = 1     #attempt

while is_failed and i <= 100 :
    print(f"Try {i}")                   #Gives condtinously 1, 2, 3............100
    i = i + 1
    
print("I give up")

# Example 4
is_failed = True
i = 1     #attempt

while is_failed:
    print(f"Try {i}")                   #using break
    i = i + 1
    if i > 100:
        break
print("I give up")

# Example 5: Print even numbers
is_failed = True
i = 1     #attempt

while is_failed:
    if i%2 != 0:
        i = i + 1
        continue
    print(f"Attempt {i}")      #using break and continue 
    i = i + 1                  
    if i > 100:
         break
print("I give up")

# Example 6: print 1 - 10

i = 0
while i <= 10:
    print(i)
    i += 1   #i = i +1
    
# Example 6: attempts - 1st 2nd iteration

i = 0
while i <= 10:
    x = 0
    while x < i:
        print("Deepa", end="-")
        x += 1
    print("")
    i += 1   #i = i +1
    
    
    
# 2. Common Example: Counting Sheep
'''Let’s relate this to a common example: Imagine you're counting sheep to fall asleep.
'''

sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    sheep_count += 1
    
# This prints "Sheep 1", "Sheep 2", and so on, until "Sheep 10". After that, the loop stops.


# 3. Avoiding Infinite Loops
'''A while loop can run indefinitely if the condition is always True. To prevent this, ensure that the condition eventually becomes False.
'''


# Example of an Infinite Loop:
# i = 1
# while i <= 5:
#     print(i)
    
    # Forgot to update i, so the condition remains True forever!
'''In this case, the loop will keep printing 1 forever because i is never incremented, so the condition i <= 5 will always be True.
To avoid this, make sure to update the variable that controls the condition within the loop.'''


# 4. Using break to Exit a while Loop
'''You can use the break statement to exit a loop when a certain condition is met.
'''
# Example:
'''Let’s stop counting sheep after 5 sheep, even though the condition allows counting up to 10:
'''
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break
    sheep_count += 1
    
'''The loop stops after "Sheep 5" because of the break statement, even though the condition was sheep_count <= 10.
'''
# Output:
# Sheep 1
# Sheep 2
# Sheep 3
# Sheep 4
# Sheep 5
# That's enough counting!

# 5. Using continue to Skip an Iteration
'''The continue statement is used to skip the current iteration and move on to the next one.
'''
# Example:
'''Let’s say you want to skip counting sheep that are number 4:
'''
sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1
    
'''Here, when sheep_count is 4, the continue statement skips printing "Sheep 4", and the loop continues with sheep_count = 5.
'''
# Output:

# Sheep 1
# Sheep 2
# Sheep 3
# Sheep 5

# 6. Using while Loops for User Input
'''You can use a while loop to repeatedly ask the user for input until they provide valid data.
'''
# Example:
'''Let’s ask the user for a PIN until they enter the correct one:
'''

pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")

'''The loop keeps running until the user enters the correct PIN.
If the user enters an incorrect PIN, they are prompted to try again.'''

# output:
'''
Enter your PIN: 1557
Incorrect PIN. Try again.
Enter your PIN: 55778
Incorrect PIN. Try again.
Enter your PIN: 1234
PIN accepted. You can proceed.'''


# example2 for only 3 trails
pin = "1234"
trails = 1

while trails<=3:
    input_pin = input(f"Trail-{trails} PIN : ")
    trails += 1
    if input_pin == pin:
      print("Correct")
      break
    else:
      print("Incorrect Password")
      
# Output:
'''
Trail-1 PIN : 5667
Incorrect Password
Trail-2 PIN : 5677
Incorrect Password
Trail-3 PIN : 1234
Correct'''