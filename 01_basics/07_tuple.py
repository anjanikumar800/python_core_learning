#############      TUPLE    ############
# tuple is ordered and immutable 

tup = (3,4,6,32,56,33)
print(tup)
del tup #  delete tuple
print(tup)
name = tuple("Anjani")
print(name)
print(type(name))

skill = ('P','Y','T','H','O','N')
print(skill)
print(type(skill))
for el in skill:
    print(el,end="   ")

# OPERATION (concatination, repition, slicing)
c = tup + skill
print(c)
print(type(c))
print(skill*3)
print(skill[0:5:1])

# membership in python

print('P' in skill)

# method and fuunction
# tuple is immutable so it have few mwthod
print(skill.index('T'))
print(skill.count('p'))

# function
# len(),max(),min(),sum(),range()
num = (34,34,65,653,34,32,44,323)
print(len(skill))
print(max(num))
print(min(num))
range() # used for looping

# program to print name of days of week when input is days of week as number
days = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
num = int(input("Enter number from (1-7) : "))
if(num<1 or num>7):
    print("invalid number..........")
    print("Enter number between 1 to 7")
    exit()
else:
    print("Today is ",days[num-1])
print("program executed sucessfully......3")