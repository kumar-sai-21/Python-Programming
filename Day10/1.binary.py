#1. Implement Binary search using recursion in a program.
#SAI KUMAR SATAPATHY

def binary_search(lists, low, high, x): 
    if high >= low:
        mid = (high + low) // 2
        if lists[mid] == x:
            return mid 
        elif lists[mid] > x: 
            return binary_search(lists, low, mid - 1, x)
        else: 
            return binary_search(lists, mid + 1, high, x)
    else:
        return -1
lists=input("Enter the Numbers in Ascending Order    ").split(' ')
print(lists)
x=input("Enter the Element to Search    ")
result = binary_search(lists, 0, len(lists)-1, x) 
if (result != -1): 
    print("Element is present at index    ", int(result)+1) 
else: 
    print("Element is not present in the list") 
