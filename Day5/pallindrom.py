 #Check for Palindrome in a string without using loop statement.
num=int(input("Enter a number"))
sum1=0
n=num
 
while num!=0:
	rem=num%10
	sum1=sum1*10+rem
	num=num/10
if sum1==n:
	print (n, "is palindrome")
else:
	print (n, "is not palindrome")
