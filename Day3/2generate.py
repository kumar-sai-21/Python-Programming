#2. Write a program which can generate and print a list and tuple where the value is square of numbers between 1 and 20(both included)
#SAI KUMAR SATAPATHY
lists=[ ]
lis=()
for i in range (1,21):
    ele=i*i
    lists.append(ele)
    lis=lis+(ele,)
print("Lists " ,lists)
print("tuple ",lis)
