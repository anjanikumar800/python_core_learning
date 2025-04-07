################     list ##################
# list is order and mutable

a = [2,5,6,8,9,34,67,24]
print(a)
print(a[0])
print(a[-1])
for val in a:
    print(val, end=" ")

print(a[2])
a[2] = 55
print(a[2])

name = ["Anjani","Ravi","Himanshu","purushottam"]
print(a + name)
print(name*3)
print(name[1:3:1])
print(name[0::1])

print("Anjani" in name) # membership test 

##############  list function and method

name.append("Prince")
print(name)

name2 = ["kumar","sharma","raj","bhumi"]
name.extend(name2)
print(name)

name.insert(2,"Priyanshu")
print(name)

name.remove("Anjani")
print(name)

name.pop()
print(name)




print(name.index("Anjani"))

print(name.count("Ravi"))

num = [5,6,3,7,1,2,9,53,34,21,67,56,90,87]
num.sort()
print(num)
num.reverse()
print(num)

#####  function
# len()
# max()
# min()
# range()

num = [5,6,3,7,1,2,9,53,34,21,67,56,90,87]
print(len(num))
print(max(num))
print(min(num))
print(range(10)) # this is used in loop

###########     EXERCISE       ####################33

# WAP to find minimum(smallest) element $ its index from a list
print("Enter element of list(length = 10) :")
num = []
for val in range(0,10,1):
    element = int(input("Enter element of %d index : " %val))
    num.append(element)
print("Given list : ",num)
print("smallest element in list is :",end=" ")
min = min(num)
print(min)
print("index of smallest number in list :",end=" ")
print(num.index(min))
print("program executed sucessfully........")

# program to find average of element of given list
print("Enter element of list(length = 10) :")
num = []
for val in range(0,10,1):
    element = int(input("Enter element of %d index : " %val))
    num.append(element)
print("Given list : ",num)
sum = 0
for el in range(0,10):
    sum += num[el]
length = len(num)
avg = sum/length
print("Average of element of given list is : ",avg)
print("program executed sucessfully........")

# program to search a given element in list
print("Enter element of list(length = 10) :")
num = []
for val in range(0,10,1):
    element = int(input("Enter element of %d index : " %val))
    num.append(element)
print("Given list : ",num)
search_element = int(input("Enter element that you want to search : "))
print("%d element found at index :"%search_element,end=" ")
print(num.index(search_element))
print("program executed sucessfully........")

# program to count number of element in list
print("Enter element of list(length = 10) :")
num = []
for val in range(0,10,1):
    element = int(input("Enter element of %d index : " %val))
    num.append(element)
print("Given list : ",num)
count_element = int(input("Enter element that to be count : "))
total_count = num.count(count_element)
print("%d element occur %d time in list"%(count_element,total_count))
print("program executed sucessfully........")