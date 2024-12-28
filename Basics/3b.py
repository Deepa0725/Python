# '''String Manipulation'''
# String concatenation

first_name = "DEEPA"
last_name = "SHREE" 
full_name = first_name + last_name
print(full_name)

full_name = first_name + " " + last_name
print(full_name)

first_word = "Good"
Second_word = "Morning"
word = first_word + Second_word
print(word)

word = first_word + " " + Second_word
print(word)


# Repetation
message = "Warning! " * 10
print(message)

NAME1 = "Deepa"
print(NAME1 * 10)


# String Methods
print(message.upper())

print(message.lower())

print(message.strip())     # Avoid the spaces

he = "DEE  "
print(he)
print(he.strip()*2)

print(message.replace("Warning! ", "Error"))    # Replace

print(he.replace("DEE", "PAA"))


txt = "I love apples , apple are my favorite fruit"    #count

x = txt.count("apple")

print(x)



name = "Deepa said 'hello'"    #single line input
print(name)
abc = 'I went to "Temple"'
print(abc)
xyz = ''' Janya said "hi"
          Deepa said "hello"
          Div said "GM" '''
print(xyz)       #Multiple line input


# Length of string includes space
print(len(message))
print(len(abc))