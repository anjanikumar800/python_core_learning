def choose(x,y,z):
    if(x>y):
        if(x>z):
            print("largest number : ",x)
        else:
            print("largest number : ",z)
    else:
        if(y>z):
            print("largest number : ",y)
        else:
            print("largest number : ",z)

choose(4,34,5)

# Exercise

# function to compute the factorial of positive number
def factorial(x):
    fact = 1
    for val in range(1,x+1,1):
        fact *= val
    return fact
print("Finding factorial")
num = int(input("Enter number : "))
if(num<0):
    print("Enter positive number")
    exit()
result = factorial(num)
print("Factorial of %d is :"%num,result)

# using function difinition of find binomial coefficient of positive interger
def factorial(x):
    fact = 1
    for val in range(1,x+1,1):
        fact *= val
    return fact
print("finding binomial coefficient nCr")
n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))
result = (factorial(n))/((factorial(r))*(factorial(n-r)))
print("Binomial coefficient :",result)
print("Program executied sucessfully.......")

# the math module
import math
print(math.sqrt(16))
print(math.ceil(4.5))
print(math.floor(4.5))
print(math.pow(5,2))
print(math.fabs(-35345)) # return absolute value means positive
# sin(),cos(),tan()