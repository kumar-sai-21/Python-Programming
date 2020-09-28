#1. Check for Palindrome in a string without using loop statement.
#SAI KUMAR SATAPATHY
string= input("Enter The String  :   ")
reverse = string[::-1]
if string==reverse:
    print("The string is PALINDROME")
else:
    print("The String is NOT A PALINDROME")
