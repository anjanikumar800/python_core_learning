######     DICTIONARY     ######

student = {"name" : "Anjani","roll no": 240010150018}
print(student)
print(type(student))
print(student["name"])
for el in student:
    print(el ,":",student[el])
student["department"] = "CSE"
for el in student:
    print(el ,":",student[el])
## del student
print(student)
print("name" in student)


# dictionary methods
print(student.get("name"))
student.clear()
print(student)
student1 = {"address":"Aurangabad", "state":"Bihar"}
student.update(student1)
print(student)

print(student)
print(student.items())
print(student.keys())
print(student.values())

# function
# len(),max(),min()
print(len(student))
print(max(student))
print(min(student))
num = {1:"Anjani",2:"Ravi",3:"Himanshu",4:"Purushottam"}
print(max(num))
print(min(num))

##  EXERCISE
# program  to build a directory of name of persons with their mobile number, and search for mobile number for given person
data = {}
i = 1
while(True):
    name = str(input("Enter name of person : "))
    mobile_number = int(input("Enter mobile number : "))
    data[name] = mobile_number
    option = str(input("Do you want to add more person(yes or no) : "))
    if(option in ["yes"]):
        continue
    else:
        break
print("finding contact number")
input_name = str(input("Enter name : "))
data_key = data.keys()
if(input_name in data_key):
    print("%s contact number : " %input_name,data[input_name])
else:
    print("Name not found")
print("Program exeuted sucessfully.....")