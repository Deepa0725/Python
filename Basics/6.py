# lists

item1 = "Books"
item2 = "Pen"                #Inefficient Way
item3 = "Pencil"
print(item1, item2, item3)

# Efficient Way

# Syntax
'''my_list = [element1, element2, element3, ...]'''

# Example1
items = ["Books", "Pencil", "Pens", "Eraser", "Scale"]
print(items)

print(items[0])         #Example for Accessing list elements  '''syntax: list_name[index]'''
print(items[-1])

# Example2
l = [1,"Books", True, [1,2,3]]
print(l)

# Example3
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example4
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Example5
mixed = ["apple", 3, True]
print(mixed)

# Example6
names = ["Deepa", "Janya", "Ram", "Sita", "Hello"]
print(names)


# Modifing the list elements

# Adding the elements
'''append(): Adds an element to the end of the list.'''          
names.append("Lakshman")
print(names)

'''insert(): Inserts an element at a specific index.'''
names.insert(0,"Hanuman")

# Removing Elements
'''pop(): Removes the element at a specific index (or the last item if no index is provided).'''     
names.pop()
print(names)

names.pop(0)  
print(names)     # To remove the particular element

names.pop(2)
print(names)

'''remove(): Removes the first occurrence of an element.'''
names.remove("Hello")
print("names")

# Example7
a = ["hi", "hello", "gm", "gm"]
print(a)

a.remove("gm")
print(a)


'''clear(): Removes all elements from the list.'''
a.clear()
print(a)


# CHANGING THE SPECIFIC ELEMENT        '''IMP''
# Example8

colors = ["pink", "red", "blue"]
print(colors)

colors[0] = "Black"
print(colors)

colors[1] = "Green"
print(colors)

# Slicing Lists

''' *start: The index to start the slice (inclusive).
    *stop: The index to stop the slice (exclusive).
    *step: The number of steps to skip elements (default is 1)'''
    
    
numbers = [0, 1, 2, 3, 4, 5, 6]                        # Syntax:    list_name[start:stop:step]
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])  
print(numbers[::2])


l = [100, 200, 300, 400]
print(l[0:4])
print(l[0::3])

l2 = l[1:3]           #Subset
print(l2)


# List Functions and Methods

'''Common Functions:'''

# len(list): Returns the number of elements in the list.
vegetables = ["Tomato", "Potato", "Chilly"]
print(len(vegetables))

# sorted(list): Returns a new sorted list without changing the original list.
numbers = [5, 9, 0, 7, 2, 1, 3]
print(sorted(numbers))
print(numbers)          # Original list remains unchanged: [5, 2, 9, 1]

# sum(list): Returns the sum of elements in a list (for numerical lists).
numbers = [1, 2, 3, 4]
print(sum(numbers))
print(numbers)

''' Common Methods:'''

# index(element): Returns the index of the first occurrence of the specified element.
Birds = ["Parrot","Peigon", "Dove", "Peacock", "Crow","Eagle"]
print(Birds)
print(Birds.index("Dove"))

# count(element): Returns the number of occurrences of an element in the list.
numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))  # Output: 3

# reverse(): Reverses the elements of the list in place.(Descending Order)
Birds.reverse()
print(Birds)  #Output:['Eagle', 'Crow', 'Peacock', 'Dove', 'Peigon', 'Parrot']

# sort(): Sorts the list in place (ascending by default).
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]


# Nested Lists
'''Lists can contain other lists, allowing you to create nested lists. This can be useful for storing matrix-like data structures.'''

# Example:1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)

# Example:2
m = [[1, 2], [3,4]]
print(m)
print(type(m))

print(m[0])
print(m[0][1])
