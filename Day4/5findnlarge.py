#Given a list A and a number n, find the n’th largest number.
#Example: If the input list is [5, 2, 1, 7, 4] and n is 3. The 3rd largest number is 4.
#SAI KUMAR SATAPATHY
lists =[]
k=int(input("Enter the number of element in the list  "))
for i in range(0,k):
    ele= int(input())
    lists.append(ele)
    
print(lists)
lists.sort()
lists =list(dict.fromkeys(lists))
print(lists)
n = int(input("Enter the nth large no you want to know  "))
if (n<k):
    print("The %d large no in the list is  " %n , end=' ')
    print(lists[n-1])
else:
    print("OUT OF RANGE")
