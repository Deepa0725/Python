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