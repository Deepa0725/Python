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