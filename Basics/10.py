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
    print(f"Try {i}")                   #Gives condtinously 1, 2, 3............
    i = i + 1
    
print("I give up")
