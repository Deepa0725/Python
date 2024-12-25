# print("Hello")  #output

# age = input("Age: ")
# print(age)

# boy_name = input("Boy Name: ")   #unformatted
# girl_name = input("Girl Name: ")

# print(boy_name + " loves " + girl_name)


boy_name = input("Boy Name: ")   
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ") 
girl_age = int(input("Girl Age: "))

age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + ". Age Difference is " + str(age_diff))  #normal

print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")   #formatted

