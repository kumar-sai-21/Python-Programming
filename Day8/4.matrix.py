#4. Run below code that will generate a matrix as an input and print all the even numbers in it
#SAI KUMAR SATAPATHY
import random
mat = [[random.randint(1,10) for i in range(4)] for row in range(4)]
print(mat)
print("")
for row in mat:
    print(row)
    print("The Even no in this row Are  ")
    for j in row:
        if(j%2==0):
            print(j)

