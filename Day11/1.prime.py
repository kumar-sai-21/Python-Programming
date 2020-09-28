#1. Write a function to check if input number is prime.
#SAI KUMAR SATAPATHY
print ("Hello, Dcoder!")
no=int(input("enter the no "))
cnt=0
for i in range(1,no+1):
  if(no%i==0):
    cnt=cnt+1
if(cnt==2):
  print("prime")
else:
  print("notprime")
  
  
  
  
  
  
  
  
  
