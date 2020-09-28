#1. Take two list of numbers and generate a list of tuples that are combo of the numbers such that two numbers in the pair are not equal
#SAI KUMAR SATAPATHY
x=input("enter the 1st set with space  ").split(" ")
y=input("enter the 2nd set with space  ").split(" ")
#print(type(x))
p=list(x)
#print(type(p))
#print(p)
z=list(y)
#print(z)
ans=[(i,j )for i in p for j in z if (i!=j)]
print (ans)