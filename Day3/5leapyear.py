#5. Write a program to find Leap Year
#SAI KUMAR SATAPATHY
year=int(input("Enter The  Year  "))
if year%4==0 and year %100!=0 or year%400==0:
    print("This is a leap year ")
else:
    print("This not a leap year")
