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


# . Accessing Tuple Elements
'''You can access elements in a tuple using indexing, just like with lists. Tuples also support negative indexing.'''

# Example3:
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry