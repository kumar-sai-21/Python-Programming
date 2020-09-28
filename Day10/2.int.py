#2. Check if the input is a valid integer - Use exception
#SAI KUMAR SATAPATHY
try:
    n=int(input("Enter The Number    "))
    print("It is an Integer  ",n)
except ValueError:
    print("its not a integer")
    
