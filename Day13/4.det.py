#4. Take a 2X2 square matrix as input and calculate the determinant:
#SAI KUMAR SATAPATHY
x=[]
y=[]
x=input(" ").split(" ")
x=[int(i) for i in x]
y=input(" ").split(" ")
y=[int(i) for i in y]
det=(x[0]*y[1])-(x[1]*y[0])
print(det)
