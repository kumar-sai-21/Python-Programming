#2. Write a program to take integral numbers and calculate the factorial.
#Note: If factorial is not defined return -1
#SAI KUMAR SATAPATHY
def myfact(no):
    if(no!=int(no) or no<0):
        return -1
    else:
        a=1
        fact=1
        while(a<=no):
            fact=fact*a
            a=a+1
        return fact
print(myfact(-1))
print(myfact(0))
print(myfact(1))
print(myfact(5))
no=int(input("enter a number to calculate factorial:"))
print(myfact(no))
    
