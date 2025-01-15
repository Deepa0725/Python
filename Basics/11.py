Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension
In this video, we will learn how to use for loops with Lists and Dictionaries, followed by advanced techniques using List Comprehension and Dictionary Comprehension. These tools are essential for writing concise and efficient Python code.

1. Looping Through Lists
A for loop is the most common way to iterate through items in a list.

Example: Sum of all numbers in a list
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)

Output:

Total sum: 150
Example: Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)
Output:

Doubled List: [2, 4, 6, 8, 10]