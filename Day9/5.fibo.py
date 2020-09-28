#5. Run a program to demonstrate Fibonacci through recursion
#SAI KUMAR SATAPATHY
def fibo(no):
    if(no==1):
        return 1
    elif(no==2):
        return 1
    else:
        return (fibo(no-1)+fibo(no-2))

no= int(input("Enter the range  "))
for no in range(1,no+1):
    print(fibo(no))