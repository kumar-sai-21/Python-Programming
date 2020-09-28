#Take an integral number N as an input and calculate the sum of first N natural numbers.
#SAI KUMAR SATAPATHY
n=int(input("Enter the Number "))
sum=0
for i in range(0,n+1):
    sum=sum+i
print("The sum of n natural no are ", sum)