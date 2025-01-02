#1 Tuple Operations:

# Create a tuple with 5 elements.
x = ("Janya", "Deepu", "Appa","Amma", "Ajji", "Maama")
print(x)

# Try to modify one of the elements. What happens?
''' x[2] = "Hello"'''   # output: x[2] = "Hello"  TypeError: 'tuple' object does not support item assignment

# Perform slicing on the tuple to extract the second and third elements.
print(x[1:3])
print(x[3:5])

# Concatenate the tuple with another tuple.
y = (1,2,3)
z = (4,5,6)
concate = y + z
print(concate)

fruits = ("Apple", "mango")
fruits1 = ("Grapes", "Banana")
fruitsall = fruits + fruits1
print(fruitsall)

all = ("Hello", 725)
all1 = ("Good Morning", 823)
comb = all + all1
print(comb)


# 2. Set Operations:

# Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
myfav = {"Apple", "Watermelon", "Mango", "Grapes"}
print(myfav)

janfav = {"Apple", "Grapes", "Litchi", "Strawberry", "Blueberry"}
print(janfav)

# Find the union, intersection, and difference between the two sets.
# UNION
union = myfav | janfav
print(union)

# INTERSECTION
inter = myfav & janfav
print(inter)

# DIFFERENCE
diff = myfav - janfav
print(diff)


# Add a new fruit to your set.
myfav.add("Litchi")
print(myfav)

janfav.add("Orange")
print(janfav)

# Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
# Remove()
myfav.remove("Apple")
print(myfav)           #WITH EXSITS

'''myfav.remove("Banana")
print(myfav)'''            #WITHOUT EXISTS  Output:  myfav.remove("Banana") KeyError: 'Banana'

# Discard()
myfav.discard("Banana")
print(myfav)

myfav.discard("Mango")
print(myfav)


# 3. Tuple and Set Comparison:

# Create a list of elements and convert it into both a tuple and a set. and Print both the tuple and the set.

my_lists = ["CAT", "DOG", "ELEPHANT", "LION", "TIGER"]
print(my_lists)
 
# To TUPLE
my_tuple = tuple(my_lists)
print(my_tuple)
      
# To SET
my_set = set(my_lists)
print(my_set)

# Try to add new elements to the tuple and set. What differences do you observe?

# Adding to tuple
tuple2 = ("Cow",) + my_tuple
print(tuple2)

# Adding to set
my_set.add("Goat")
print(my_set)