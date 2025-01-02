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


# Empty Set:
'''To create an empty set, use the set() function (not {}, which creates an empty dictionary).'''

empty_set = set()   
# s = {}   - it is dictionary not set

