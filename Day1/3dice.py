#You are given a cubic dice with 6 faces. All the individual faces have a number printed on them.
#The numbers are in the range of 1 to 6, like any ordinary dice.
#Input a dice face number, and output the opposite face number
#SAI KUMAR SATAPATHY(190310248)


x=int(input("Enter the no on the face "))
opposite= (7-x)
if(x>0)and(x<7):
    print("The opposite face have the no:",opposite)
else:
    print("Number is not in the DIce")
