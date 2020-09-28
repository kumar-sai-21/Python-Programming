# Find sum of digits in a number
#SAI KUMAR SATAPATHY
num=int(input("Enter The Number "))
add=0
while (num > 0):
    x=num%10
    add= add+x
    num=num//10
print("sum of the dight in the number are: " ,add)