#write a program that takes two matrices as input and does matrix multiplication

r1,c1=input("enter the number of rows and column of 1st matrix:").split()
r1,c1=int(r1),int(c1)
print("enter 1st matrix elements:")
x=[[int(input()) for i in range(c1)] for j in range(r1)]
print("Matrix 1:")
for item in x:
    print(item)

r2,c2=input("enter the number of rows and column of 2nd matrix:").split()
r2,c2=int(r2),int(c2)
print("enter 2nd matrix elements:")
y=[[int(input()) for i in range(c2)] for j in range(r2)]
print("Matrix 2:")
for item in y:
    print(item)
    
r=0
result=[[r for i in range(c2)] for j in range(r1)]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
print("\nresultant matrix after multiplication:")
for item in result:
    print(item)
