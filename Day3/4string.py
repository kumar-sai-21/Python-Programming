#4. WAP that can accept two strings as input and print the string with maximumlength in console.
#If two strings have the same length, then the program should print both the strings line by line
#SAI KUMAR SATAPATHY
str1=input("Enter The First String ")
str2=input("Enter The Second String ")
l1=len(str1)
l2=len(str2)
if l1==l2:
    print(str1)
    print(str2)
elif l1>l2:
    print(str1,l1)
else:
    print(str2,l2)
