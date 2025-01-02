# Sets in Python
'''A set is a collection of unique items that is unordered and unindexed. Sets do not allow duplicate values. 
Sets are useful for performing operations like union, intersection, and difference.'''

# Syntax:
'''my_set = {element1, element2, element3, ...}'''


fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
print(fruits_set)
print(numbers_set)

s = {10, 200, 3}       # set is unordered  output:{200, 10, 3}
print(s)

# print(s[0])    Set is unindexed

s2 = set((1, 2, 3))        #Another form for declare sets
print(s2)
print(type(s2))


#1 Empty Set:
'''To create an empty set, use the set() function (not {}, which creates an empty dictionary).'''

empty_set = set()   
# s = {}   - it is dictionary not set


# 2. Set Operations
'''Sets support mathematical operations like union, intersection, and difference.'''

# Union:(OR)
'''The union of two sets combines all elements from both sets, removing duplicates.'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
print(union_set)

# Intersection:(AND)
'''The intersection of two sets returns elements that are common to both sets.'''

intersection_set = set1 & set2  # Output: {3}
print(intersection_set)

# Difference:
'''The difference between two sets returns elements that are in the first set but not in the second.'''

difference_set = set1 - set2  # Output: {1, 2}
print(difference_set)

# Symmetric Difference:
'''The symmetric difference returns elements that are in either of the sets but not in both.'''

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
print(sym_diff_set)


#3. Set Methods
'''Sets come with several useful methods for performing common tasks.'''

# add(): Adds an element to the set.
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}


# remove(): Removes a specified element from the set. Raises an error if the element does not exist.
fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple','orange', 'cherry'}

'''fruits_set.remove("Mango")
print(fruits_set)      #keyerror:mango
'''
# discard(): Removes a specified element without raising an error if it does not exist.
fruits_set.discard("banana")  # No error if "banana" is not in the set
print(fruits_set)

# pop(): Removes a random element from the set.
fruits_set.pop()
print(fruits_set)


# clear(): Removes all elements from the set.
fruits_set.clear()
print(fruits_set)


# 9. Differences Between Lists, Tuples, and Sets
'''Feature	  List	                Tuple	            Set
Ordering	  Ordered	            Ordered	            Unordered
Mutability	  Mutable	            Immutable	        Mutable
Duplicates	  Allows duplicates	    Allows duplicates	No duplicates
Indexing	  Supports indexing	    Supports indexing	No indexing
Operations	  List operations	    Tuple operations	Set operations
Common Uses	  General collection	Fixed data	        Unique items'''