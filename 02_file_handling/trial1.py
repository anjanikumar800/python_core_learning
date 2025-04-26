# read
file = open("file_handling/trial1.txt", "r")

content = file.read()
print(content)
content1 = file.readline()
print(content1)
content2 = file.readline()
print(content2)
file.close()

file = open("file_handling/trial1.txt","r")
# using for loop
for el in file:
    print(file.readline())
file.close()

try:
    file = open("file_handling/trial1.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File doesn't Exist")
except PermissionError:
    print("Permission denied!")

# write
file = open("file_handling/trial2.txt","w")
file.write("This is trial\n")
file.close()

file = open("file_handling/trial2.txt","a")
file.write("This is second trial")
file.close()