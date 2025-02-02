#Finding the even or odd
number = input("Enter a number: ")
x = int(number)%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
    
    
# #to convert the temperature in degree centigrade to Fahrenheit
c = input("Enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is: ", f)

# to find the area of a triangle whose sides are given
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)

# to find out the average of a set of integers
count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)


# program to find the product of a set of real numbers
i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)


# program to find the circumference and area of a circle with a given radius
import math
r = float(input("Input the radius of the circle: "))
c = 2 * math.pi * r
area = math.pi * r * r
print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)


#program to check whether the given integer is a multiple of 5
number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")
    
# program to check whether the given integer is a multiple of both 5 and 7
number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")
    
    
#program to display the given integer in a reverse manner
number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)

# program to find the geometric mean of n numbers
c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)


# program to display all integers within the range 100-200 whose sum of digits is an even number
for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
        
        
# program to check whether the given integer is a prime number or not
num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
# program to find the factorial of a number using recursion
def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)



# program to find the roots of a quadratic equation
import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")