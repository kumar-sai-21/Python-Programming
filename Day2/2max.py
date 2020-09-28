#Find the maximum element in the list without using max function
#SAI KUMAR SATAPATHY
a=[12,45,76,35,87,95,133,665]
high=a[0]
for i in a:
    if(i>high):
        high=i
print("The maximun no in the list is ",high)
