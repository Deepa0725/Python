#Example Programs

# Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " you are " + age + " years old")
print(f"Hello {name} You are {age} years old")


'''String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace. '''

sentence = ("Python is Awesome! ")
print(sentence)
print(sentence.lower())
print(sentence.upper())
print(sentence.replace(" ", "_"))
print(sentence.strip())