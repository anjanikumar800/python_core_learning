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