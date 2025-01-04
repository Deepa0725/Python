# DICTIONARIES

# A dictionary in Python is a collection of key-value pairs. Each key in a dictionary is associated with a value, and you can retrieve or 
# manipulate data using the key. Unlike lists and tuples, dictionaries are unordered and mutable (changeable).

# 1. Creating a Dictionary
'''You can create a dictionary using curly braces {} or the dict() function.'''

# Syntax:
'''my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}'''

# Example1 
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food)

# Example2
Birthday = {
    "Deepa" : "07-05-2002",
    "Janni" : "24-02-2006",
    "Virat" : "05-1-1988"
}
print(Birthday)
print(type(Birthday))


# 2. Accessing Dictionary Elements
'''To access the values stored in a dictionary, you use the key.'''

# Example1:(cont)
print(karnataka_food["Mysuru"])  # Output: Mysore Pak

'''can also use the get() method to access values, which is safer because it doesn’t throw an error if the key doesn’t exist.'''
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found

# Example2:(cont)
print(Birthday["Janni"])

print(Birthday.get("Deepa"))
print(Birthday.get("Hello","Not Found"))


# 3. Adding and Updating Dictionary Elements
'''can add new key-value pairs or update existing values in a dictionary.'''

# Adding an Item:
karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)

Birthday["Appa"] = "01-11-1969"
print(Birthday)

# Updating an Item:
karnataka_food["Bengaluru"] = "Ragi Mudde"
print(karnataka_food)



# 4. Removing Elements from a Dictionary
'''can remove items from a dictionary using several methods:'''

# pop(): Removes the specified key and returns the associated value.
mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak
print(karnataka_food)

print(Birthday)
x = Birthday.pop("Virat")
print(Birthday)
print(x)

# del: Removes the specified key.
del karnataka_food["Mangaluru"]
print(karnataka_food)

# clear(): Empties the dictionary.
karnataka_food.clear()
print(karnataka_food)