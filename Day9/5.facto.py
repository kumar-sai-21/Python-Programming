#5. Run a program to demonstrate Factorial through recursion
#SAI KUMAR SATAPATHY
def fact (no):
    if(no==1):
        return 1
    elif(no<1):
        return 'not valid no'
    else:
        return (no*fact(no-1))
no=int(input("ENter the no "))
print(fact(no))