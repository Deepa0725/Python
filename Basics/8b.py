# PRACTICE

#1. Basic Dictionary Operations:
'''Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.'''
karnataka = { 
             "Bangalore" : "Jamoon",
             "Mysore" : "Mysore Pak",
             "Davangere" : "Benne Dose",
             "Darwad" : "Peda",
             "Hubli" : "Girmit"
             }
print(karnataka)

'''Add a new city and its dish to the dictionary.'''

karnataka["Mangalore"] = "Bajji"
print(karnataka)

'''Update the dish for Bengaluru.'''
karnataka["Bangalore"] = "Bisi Bele Bath"
print(karnataka)

'''Remove one city from the dictionary.'''
kar = karnataka.pop("Mangalore")    #Using Pop method
print(kar)
print(karnataka)

del karnataka["Hubli"]
print(karnataka)    #Using Del

'''Use the keys() method to print all city names in the dictionary.'''
print(karnataka.keys())
print("Cities: ", karnataka.keys())

'''Use the values() method to print all dishes in the dictionary.'''
print(karnataka.values())
print("Dishes: ", karnataka.keys())

# 2. Nested Dictionary Practice :

'''Creating a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.'''
friends_details = {
    "Friend1" : {
        "Name" : "Janya",
        "Favourite subject" : "Science",
        "Favourite Food" : "Chicken"
    },
   "Friend2" : {
        "Name" : "Saniya",
        "Favourite subject" : "Maths",
        "Favourite Food" : "Pizza"
    }
}

print(friends_details)

'''Access and print the favorite food of one friend.'''

print("Favourite food of Friend1: ", friends_details["Friend1"]["Favourite Food"])

'''Access and print the favorite subject of one friend.'''

print("Favourite subject of Friend2: ", friends_details["Friend2"]["Favourite subject"])