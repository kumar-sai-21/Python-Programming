#3.With a given integral number n, write a program to generate a dictionary that
#contains (i, i*i) such that is an integral number between 1 and n (both included) and
#then the program should print the dictionary.
#SAI KUMAR SATAPATHY
def my_dic(no):
    d={i:i**2 for i in range(1,no+1)}
    print(d)

no =int(input("Enter the no  "))
my_dic(no)