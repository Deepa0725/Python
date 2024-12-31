#1111 List Manipulation Exercise:

# Create a list of 5 items (strings or numbers).
places = ["Bangalore", "Mysore", "Goa", "Mangalore"]
print(places)

# Add a new item to the end of the list and another at the second position.
places.append("Shivamogga")
print(places)

places.insert(2,"Udupi")
print(places)

# Remove the third item from the list.
places.pop(4)
print(places)


#22222 Reverse and Sort a List: Create a list of numbers :

nums = [30, 80, 10, 100, 40, 20]
print(nums)
print(sorted(nums))

# Sort it in descending order.(reverse order)
nums.reverse()
print(nums)

# Sort it in ascending order
nums.sort()
print(nums)

# Reverse the sorted list and print it (descending order)
nums.reverse()
print(nums)
