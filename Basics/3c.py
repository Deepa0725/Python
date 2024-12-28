# Accessing String Characters
name = "Deepa"
print(name[1])
print(name[4])     #Index= position - 1
print(name[3])


# String Slicing
print(name[2:5])

abc = "Bangalore"
print(abc[0:7])
print(abc[0:8])
print(abc[0:9])
print(abc[:8])
print(abc[0:])
print(abc[2:6])

#Reverse Indexing  [-4,-3,-2,-1]
print(abc[-4])

#Getting the alernative  [start:end: skip/step]
print(abc[::])
print(abc[::1])
print(abc[::2])
print(abc[::3])
print(abc[::4])
print(abc[::5])

# Escape Sequence (Starts with aback slash)
s = "Deepa is a \nGood Girl"     #Enter
print(s)

s = "Deepa is a \tGood Girl"     #Tab
print(s)

