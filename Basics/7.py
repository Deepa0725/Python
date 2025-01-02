# Tuples: A tuple is a collection of items that is ordered and immutable (unchangeable).

# Syntax:
'''my_tuple = (element1, element2, element3, ...)'''

# Example1
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
numbers_tuple = (1, 2, 3, 4)
print(numbers_tuple)

# Example2
genders = ("Male", "Female", "Others")
print(genders)

print(type(genders))
print(len(genders))
print(genders[0])
print(genders[1])
print(genders[1:3])

# Creating a Tuple with One Element:
'''To create a tuple with only one element, include a trailing comma:'''

single_element_tuple = ("apple",)
print(single_element_tuple)


#2 . Accessing Tuple Elements
'''You can access elements in a tuple using indexing, just like with lists. Tuples also support negative indexing.'''

# Example3:
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Slicing tuples to acces the subset
print(fruits[1:3])  # Output: ('banana', 'cherry')            


#3 Tuple Operations

# Tuple Concatenation:
'''You can combine two or more tuples using the + operator.'''

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple Repetition:
'''You can repeat a tuple multiple times using the * operator.'''

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Checking Membership:
'''You can check if an item exists in a tuple using the ''in'' operator.'''

print("apple" in fruits)  # Output: True

print("hello" in fruits)  #Output: False