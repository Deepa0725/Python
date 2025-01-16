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

Example: Printing Kannada food items
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")
Output:

I like Dosa
I like Idli
I like Vada
I like Bisibelebath


2. Looping Through Dictionaries
You can use for loops to iterate over dictionaries by accessing both keys and values.

Example: Iterating over dictionary keys
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)
Output:

Anand
Geetha
Kumar

Example: Iterating over dictionary values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)
Output:

85
90
78

Example: Iterating over both keys and values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")
Output:

Anand scored 85 marks
Geetha scored 90 marks
Kumar scored 78 marks


3. for Loops with range()
You can also use for loops with the range() function to loop through a sequence of numbers.

Example: Adding marks to students using index values
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)

Output:

{'Anand': 85, 'Geetha': 90, 'Kumar': 78}