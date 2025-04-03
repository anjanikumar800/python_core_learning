##############             string      ####################
# string is order and immutable
full_name = "Anjani Parashar"
sur_name = " Sharma"
print(full_name)
print(full_name[0])
print(full_name[-1])
print(full_name[-4])
print(full_name[0:3])
print(full_name[-3:-1])
print(full_name+sur_name)
print(full_name*5)

# program to print all vowel of full_name
count=0
for el in full_name:
    if(el in ['a','e','i','o','u']):
        count+=1
        print(el, end=" ")
print("no. of vowel =",count)

# program to count number of character in given string
ch= str(input("Enter string : "))
count=0
for val in ch:
    count+=1
print("no. of character in %s is ="%(ch),count)

###########  membership test on string
print('An' in full_name)
print('Ab' in full_name)


#############   string method and function      #############

txt = "hello, world"
print(txt.capitalize())
print(txt.count('l'))
print(txt.startswith('h'))
print(txt.endswith('d'))
print(txt.find('e'))
print(txt.index('l'))
print(txt.isalnum())
print(txt.isalpha())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.islower())
print(txt.isnumeric())
print(txt.isprintable())
print(txt.isspace())
print(txt.istitle())
print(txt.isupper())
print(txt.lower())
print(txt.partition('hel'))
print(txt.replace('world','india'))

# FUNCTION
# char()
# ord()
# len()
# str()


# program to check given word is palindrome or not
character= str(input("write word : "))
ch = character.lower()
ch_length = len(ch)

# using slice
if(ch==ch[::-1]):
    print("given word is palindrome")
else:
    print("given word is not palindrome")

# using loop

for el in range(0,ch_length):
    if(ch[el]!=ch[(ch_length-1)-el]):
        print("given word is not palindrome")
        exit()
else:
    print("given word is palindrome")

# program that read a word in lowercase and capitalize alternative letter
txt = str(input("Enter word : "))
txt_length = len(txt)
new_txt =""
temp = "true"
for el in range(0,txt_length):
    if(temp=="true"):
        new_txt+=txt[el].upper()
        temp="false"
    else:
        new_txt+=txt[el]
        temp="true"
print(new_txt)