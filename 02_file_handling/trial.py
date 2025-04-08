# writing
f = open("02_file_handling/trial.txt",'w')
f.write("Hey i am Anjani\n")
f.write("currently learning python")
f.close()

# reading
f = open("02_file_handling/trial.txt","r")
r1 = f.read()
print(r1)
f.close()

print(f.closed) # print True or False
print(f.mode) # print in which mode file is open
print(f.name) # print name of file

file_object = open("02_file_handling/trial2.txt","w")
file_object.write("i am anjani kumar from bihar\n")
file_object.write("currently learning python")
print(file_object.tell()) # print current location of pointer strating from 0
file_object.close()

file_object = open("02_file_handling/trial2.txt","r+")
content = file_object.read(12)
print(content)
print(file_object.tell())
file_object.seek(3)  # move pointer to that particular location
file_object.write("Parashar")
print(file_object.read())


import os
os.rename("old_file_name","new_file_name") # rename file
os.remove("new_file_name") # delete file
os.mkdir("my_folder") # create a new folder
os.chdir("python/01_file_handling")    # change (fix location of working folder) working directory
os.rmdir("directory_name")  # delete directory
print(os.getcwd()) # getting current working directory
print(os.listdir())  # list of file and directories