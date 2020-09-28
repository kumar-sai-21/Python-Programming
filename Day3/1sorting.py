#1. Find if a list is sorted in increasing order
#SAI KUMAR SATAPATHY
lists=[]
n=int(input("enter number of elements="))
for i in range(0,n):
    ele=int(input())
    lists.append(ele)
j=1
for i in range(0,n-1):
    if(lists[i]<=lists[i+1]):
        j=j+1
    else:
        break
if(j==n):
    print("list is sorted")
else:
    print("unsorted")
