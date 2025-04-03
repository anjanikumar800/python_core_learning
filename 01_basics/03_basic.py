###################                 decision making and loop               ##########################
"""
range() function
for loop , while loop , break, continue, nested loop
"""

for el in range(0,5,1):
    print(el)

# WAP to find sum of first n natural number

num = int(input("Enter number : "))
sum = 0
for el in range(1,num+1):
    sum+=el

print("sum of first %d natural number : " %(num),sum)



# WAP to print 50 positive number , 10 number in each line

for el in range(1,51):
    print(el, end=" ")
    if(el % 10 == 0):
        print()
print("done.......")


# WAP to find sum of even and odd number lies between 1 to 100
even_sum=0
odd_sum=0
for val in range(1,101):
    if(val % 2 ==0):
        even_sum += val
    else:
        odd_sum += val
print("sum of even number : ", even_sum)
print("sum of odd number : ", odd_sum)


# WAP to find factorial of a number 'n'

num = int(input("Enter number : "))
fact = 1
for el in range(num,1,-1):
    fact = fact*el
print("factorial  = ",fact)


# WAP to print first n multiple of natural number

num = int(input("Enter number that you want to find multiple : "))
n = int(input("Enter value of n : "))
for el in range(1,n+1):
    print(num*el, end="  ")




#################     while loop          


# WAP to print sum of first 100 natural number using while loop

i = 1
sum=0
while(i<=100):
    sum += i
    i += 1
print("sum of first 100 natural number is ",sum)


# WAP to find sum of even and odd number between 1 to 100

i = 1
even_sum = 0 
odd_sum = 0
while(i<=100):
    if(i % 2 == 0):
        even_sum += i
    else:
        odd_sum += i
    i += 1
print("Even sum =",even_sum)
print("odd sum =",odd_sum)


# WAP to find sum of digit of natural number
num = int(input("Enter number : "))
result = 0
while(num != 0):
    rem = num %10
    num //= 10
    result += rem
print("sum of digit =",result)


# WAP to find largest digit of a natural number
num = int(input("Enter number : "))
max = 0
while(num != 0):
    rem = num %10
    num //= 10
    if(rem > max):
        max = rem
print("largest digit :", max)




##########   nested loop       #################

# program to print following pattern using nested for loops
# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for el in range(1,6):
    for val in range(1,el+1):
        print(el, end=" ")
    print()

# program to print following pattern
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

for el in range(1,6):
    for val in range(6,el,-1):
        print(6-el, end=" ")
    print()

# program to print following pattern 
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for el in range(1,6):
    for val in range(1,el+1):
        print(val, end=" ")
    print()

# program to print following table
# * 
# * * 
# * * *
# * * * *
# * * * * *

for el in range(1,6):
    for val in range(1,el+1):
        print("*", end=" ")
    print()

# program to check whether given whole number is prime or not using for loop
import math
num = int(input("Enter positive number : "))
m = int(math.sqrt(num))
if(num==1):
    print("not prime")
    exit()
elif(num==2):
    print("prime")
    exit()
for el in range(2,m+1):
    if(num % el == 0):
        print("not prime")
        break
else:
    print("prime number")

# program to check whether given whole number is prime or not using while loop
import math
num = int(input("Enter positive number : "))
m = int(math.sqrt(num))
if(num==1):
    print("not prime")
    exit()
elif(num==2):
    print("prime")
    exit()
i = 2
while(i<=m):
    if(num%i==0):
        print("not prime")
        break
    i+=1
else:
    print("prime number")

# program to print first 'n' prime number
import math
n = int(input("Enter value of n : "))
count=0
i = 2
while(count<n):
    for el in range(2,int(math.sqrt(i))+1):
        if(i % el == 0):
            break
    else:
        count+=1
        print(i, end=" ")
    i+=1
print()
print("program executed sucessfully.............")

# program to print first nth term of prime number
import math
n = int(input("Enter value of n : "))
count=0
i = 2
while(count<n):
    for el in range(2,int(math.sqrt(i))+1):
        if(i % el == 0):
            break
    else:
        count+=1
        nth_prime= i
    i+=1
print("nth prime is ",nth_prime)
print("program executed sucessfully.............")

# program to find HCF of two whole number
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
n1=num1
n2=num2
rem=1
while(rem!=0):
    rem = num2%num1
    num2=num1
    num1=rem
print("HCF of %d and %d is :"%(n1,n2),num2)

# program to check whether a given number is armstrong number or not
num = int(input("Enter number : "))
m=num
n=num
count =0 
result = 0
while(num != 0):
    rem = num %10
    num //= 10
    count+=1
while(n!=0):
    rem = n%10
    n//=10
    result+=(rem**count)
if(result==m):
    print("%d is Armstrong number"%(m))
else:
    print("%d is not Armstrong number"%(m))

# program to print first n term of fibonacci series
n = int(input("Enter n value : "))
n1=0
n2=1
if(n==1):
    print("0")
    exit()
elif(n==2):
    print("0 1")
    exit()
print("0 1",end=" ")
for el in range(3,n+1):
    result = n1+n2
    n1=n2
    n2=result
    print(result,end=" ")


# program to print first 'nth' terms of Fibonacci series
n = int(input("Enter nth value : "))
n1=0
n2=1
if(n==1):
    print("1st term of Fibonacci series is :",n1)
    exit()
elif(n==2):
    print("2nd term of Fibonacci series is :",n2)
    exit()
for el in range(3,n+1):
    result = n1+n2
    n1=n2
    n2=result
print("%dth term of Fibonacci series is : "%(n),result)


# program to check whether given naumber is palindrome or not
num = int(input("Enter number : "))
n=num
result=0
while(num!=0):
    rem = num%10
    num//=10
    result = result*10 +rem
if(result==n):
    print("%d is palindrome"%(n))
else:
    print("%d is not palindrome"%(n))