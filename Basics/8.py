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


# 2. Accessing Dictionary Elements
'''To access the values stored in a dictionary, you use the key.'''

# Example1:(cont)
print(karnataka_food["Mysuru"])  # Output: Mysore Pak

'''You can also use the get() method to access values, which is safer because it doesn’t throw an error if the key doesn’t exist.'''
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found

# Example2:(cont)
print(Birthday["Janni"])

print(Birthday.get("Deepa"))
print(Birthday.get("Hello","Not Found"))