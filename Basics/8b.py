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
