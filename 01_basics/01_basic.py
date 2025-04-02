 ############                                 Standard input/output                              ############### 


 num1 = int(input("Enter number : "))
print("Entered number is =",num1)

num2 = float(input("Enter number : "))
print("Entered number is =",num2)

num3 = str(input("Enter name : "))
print("Entered number is =",num3)

print(type(num1))
print(type(num2))
print(type(num3))

# program to calculate average of three number

num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))
num3 = float(input("Enter 3rd Number : "))

total = num1+num2+num3
print("Average = ", round(total/3,2))

print("India is my country", "and all indian are my brother", "and not sister", sep='...', end='$')
print()
print("india is my country\n and all indian are my brother\n and not sister")
print(""" india is 
      my country and 
      all indian are my 
      brother and not sister """)

print("my name is %s and my age is %d" %("Anjani Kumar" , 19))

name1 ="Anjani"
print(id(name1)) # print address location of name
print(name1)
name2 ="Anjani"
print(id(name2)) # print address location of name
print(name2)
# both name and name2 have same addess location


# WAP to find sum of digits of 4-digit positive number

num = int(input("Enter 4-digit number : "))
number = num
rem1 = num%10
num = num//10
rem2 = num%10
num = num//10
rem3 = num%10
num=num//10
rem4 = num%10

total = rem1+rem2+rem3+rem4
print(type(total))
print("Sum of digits of " ,number, " is = ",total )



# WAP to print 4-digit number in reverse order

num = int(input("Enter 4-digit number : "))
number = num
rem1 = num%10
num = num//10
rem2 = num%10
num = num//10
rem3 = num%10
num=num//10
rem4 = num%10

reverse = rem1*1000 + rem2*100 + rem3*10 + rem4
print("reverse number = ",reverse)


# WAP to convert time in seconds to time in hours, minute and second

total_second = int(input("Enter total time in second : "))
second = total_second % 60
rem = total_second // 60
minute = rem % 60
hours = rem // 60
print("hours = ", hours)
print("minute = ", minute)
print("second = ", second)


# WAP to find area of triangle whose side are given
import math
side1 = float(input("Enter lenght of 1st side of triangle : "))
side2 = float(input("Enter lenght of 2nd side of triangle : "))
side3 = float(input("Enter lenght of 3rd side of triangle : "))

s = (side1 + side2 + side3)/2
area = round(math.sqrt(s*(s-side1)*(s-side2)*(s-side3)),3)
print("Area of triangle =",area)


#WAP to calculate simple interest and compound interest

principle = float(input("Enter principle : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))
simple_interest = (principle*rate*time)/100
compound_interst = round( (principle*((1+(rate/100))**time)) - principle , 3)
print("simple interest =",simple_interest)
print("compond interest =",compound_interst)


# WAP to swap two number 
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

print("before swapping 1st number : ", num1)
print("before swapping 2nd number : ", num2)
print("swapping......")

t=num1
num1=num2
num2=t
print("After swapping 1st number : ", num1)
print("After swapping 2nd number : ", num2)


#  second way to swap without using third variable

num1,num2 = num2,num1

print("After swapping 1st number : ", num1)
print("After swapping 2nd number : ", num2)


# third way

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("After swapping 1st number : ", num1)
print("After swapping 2nd number : ", num2)