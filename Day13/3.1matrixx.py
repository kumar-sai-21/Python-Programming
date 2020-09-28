# Program to multiply two matrices using nested loops


matrix1= [[1,4,3],
    [4 ,5,78],
    [1 ,18,93]]

matrix2 = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

multi = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(matrix1)):
   for j in range(len(matrix2[0])): 
       for k in range(len(matrix2)):
           multi[i][j] += matrix1[i][k] * matrix2[k][j]

for r in multi:
   print(r)
