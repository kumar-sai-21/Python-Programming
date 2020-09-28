#Take a string as input and do the following without using any string functions:
#      i. Remove if there are any duplicates
#      ii. Remove if there are any special characters
#      iii. Change the case of each character 

x=input("Enter the string:")
s=" "

for i in x.split():
    if i not in s:
        s=s+i+" "
print("Duplicates removed:")
print(s)
s=" "
for i in x:
    if(ord(i)>=97 and ord(i)<=122 or ord(i)==32 or ord(i)>=65 and ord(i)<=90):
        s=s+i
print("Special characters removed:")
print(s)
s=" "
for i in x:
    if (ord(i)>=97 and ord(i)<=122):
        s=s+chr(ord(i)-32)
    elif (ord(i)>=65 and ord(i)<=90):
        s=s+chr(ord(i)+32)
    else:
        s=s+i
print("Changed case:")
print(s)
        
