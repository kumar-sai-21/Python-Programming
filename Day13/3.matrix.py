#MULTIPLY TWO MATRIX
#SAI KUMAR SATAPATHY

#def multiply(matrix1,matrix2,r,c):
 #   multi=[]
  #  for i in range(len(matrix1)):
   #     for j in range (len(matrix2)):
    #        for k in range(len(matrix2)):
     #           multi[i][j]+=matrix1[i][j]*matrix2[i][j]
   # for r in multi:
    #    print(r)
r=int(input("Enter the no of ROW of the matrix "))
c=int(input("ENter the no of COLUMn of the Matrix "))
matrix1=[]
matrix2=[]
print("Enter element in 1st matrix")
print("enter the entries row:")
for i in range (r):
    a=[]
    for j in range (c):
        a.append(int(input()))
    matrix1.append(a)
for i in range (r):
    for j in range (c):
        print(matrix1[i][j],end=" ")
    print()
print("Enter the element in second matrix ")
print("enter the entries row:")
for i in range (r):
    a=[]
    for j in range (c):
        a.append(int(input()))
    matrix2.append(a)
for i in range (r):
    for j in range (c):
        print(matrix2[i][j],end=" ")
    print()
#multiply(matrix1,matrix2,r,c)
multi=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(matrix1)):
    for j in range (len(matrix2[0])):
        for k in range(len(matrix2)):
            multi[i][j]+=matrix1[i][k]*matrix2[k][i]
for r in multi:
    print(r)