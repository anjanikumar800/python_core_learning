#####    Sets    ######
# set are unordered and elements are immutable but whole set are mutable

num1 =  {2,7,43,56,434}
num2 = set([2,5,34,54,343])
num3 = set("49825")
name = set("Anjani")
print(num1)
print(num2)
print(num3)
print(name)

days = {'mon','tue','wed','thu','fri','sat','sun'}
for el in days:
    print(el,end=" ")

# Adding and removing element in set

veg = set(['potato','tomato','brinjal'])
print(veg)
veg.add('cucumber')
print(veg)
veg.remove('brinjal')
print(veg)

# union(|) and intersection(&) and difference
# difference means a new set containing only elements from the first set and none from the second set
a={0,2,3,5}
b={-1,2,3,7,9}
a_union_b = a|b
a_intersection_b = a&b
a_difference_b = a-b
print(a_union_b)
print(a_intersection_b)
print(a_difference_b)