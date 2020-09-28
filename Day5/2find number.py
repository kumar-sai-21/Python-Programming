#find a number in a list
#SAI KUMAR SATAPATHY
list1=input("enter the numbers to the list with commas")
print(list1)
x=list1.split()
n=input("enter the number to search")
z=x.count(n)
if(z==0):
    print("not found at index:")
else:
   print("found")
 
