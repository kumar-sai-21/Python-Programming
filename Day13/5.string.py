#SAI KUMAR SATAPATHY
x=input("Enter the string:")
s=" "

for i in x.split():
    if i not in s:
        s=s+i+" "
print("Duplicates Removed:")
print(s)
s=" "
for i in x:
    if(ord(i)>=97 and ord(i)<=122 or ord(i)==32 or ord(i)>=65 and ord(i)<=90):
        s=s+i
print("Special characters Removed:")
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
        

