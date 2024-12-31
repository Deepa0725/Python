# 1. Python list of strings
groceryList = ["Rice","Wheat","Barley"]
print(groceryList)

# 2. Python list of numbers
myNumbers = [1,5,9,16,28]
print(myNumbers)

# 3. Python list with duplicate values
myNumbers = [1,5,5,9,9,9,16,28]
print(myNumbers)

# 4. Python list that contains different data type values
heterogeneousList = ["Python",123,24.5,True,35,"a"]
print(heterogeneousList)

# 5. Finding the length of a list in Python
ProgrammingList = ["CSharp","Python","PHP","R"]
print(len(ProgrammingList))

# 6. Finding the index of items in a Python list
fruits = ["apple","banana","mango"]
bananaIndex = fruits.index("banana")
mangoIndex = fruits.index("mango")
print(bananaIndex)
print(mangoIndex)

pythonList = ["p","y","t","h","o","n"]

# to get the 1st item
print(pythonList[0])

#to get the 4th item
print(pythonList[3])

# Negative indexing to get last item
print(pythonList[-1])

# To get second last item
print(pythonList[-2])

# 7. Slicing of lists in Python
myList = ['p','y','t','h','o','n','i','s','t','a']

# elements from 5 to 8
print(myList[4:8])

# from 1st element to 4th element
print(myList[:4])

# from 8th element to last element 
print(myList[7:])

# from 1st to last elements
print(myList[:])

# negative slicing
print(myList[-1:-9])

print(myList[-5:])

print(myList[:-4])