######################       decision making and branching        ############################

#  WAP to find largest of three number using if statement

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

max=num1

if(num2>max):
    max=num2

if(num3>max):
    max=num3

print("largest number = ",max)

# second method

if(num1 > num2):
    if(num1>num3):
        print("largest number is ",num1)
    else:
        print("largest number is ",num3)
else:
    if(num2>num3):
        print("largest number is ",num2)
    else:
        print("largest number is ",num3)


#  WAP to print largest of two number

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if(num1 > num2):
    print("largest number : ",num1)
else:
    print("largest number : ",num2)


# WAP to test weather the number is positive or negative , if number is positive then check even or odd

num = int(input("Enter number : "))

if(num > 0):
    print("Entered number is positive")
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")

elif(num==0):
    print("Zero")

else:
    print("Entered number is negative")


#  WAP to print name of days of week when we are given day of week as number from 0-7

days = int(input("Enter number(1-7): "))
print("Loading.....")

if(days==1):
    print(" Today is Sunday")
elif(days==2):
    print(" Today is Monday")
elif(days==3):
    print(" Today is Tuesday")
elif(days==4):
    print(" Today is Wednesday")
elif(days==5):
    print(" Today is Thursday")
elif(days==6):
    print(" Today is Friday")
elif(days==7):
    print(" Today is Saturday")
else:
    print("invalid number.....")


#  WAP to find root of quadratic equation coefficient of x^2 is 'a' and coefficient of x is 'b' and constant term 'c'
import math
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
d= (b*b)-(4*a*c)

if(d<0):
    print("real part root : ",(-b)/(2*a))
    print("imaginary part root : ",math.sqrt(-d)/(2*a))
elif(d==0):
    print("equal root : ",-b/(2*a))
else:
    print("root one : ",((-b)-(math.sqrt(d)))/(2*a))
    print("root two : ",((-b)+(math.sqrt(d)))/(2*a))


#  WAP to determine whether given year is leap year or not

year = int(input("Enter year : "))
if((year % 4 ==0 and year % 100 != 0) or (year % 400 == 0)) :
    print("Leap year")
else:
    print("not a leap year")