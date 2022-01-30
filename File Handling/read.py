# Example1
# read only first 2 character of a file

file = open("demofile.txt", "r")
print(file.read(2))

# Example2
# read the complete file
file = open("demofile.txt", "r")
print(file.read())

# example 3
# reading line by line

file = open("demofile.txt", "r")
print(file.readline())


file = open("demofile.txt", "r")
print(file.readline())



file = open("demofile.txt", "r")
print(file.readlines(15))

import os
file=open("demofile.txt","r")
for line in file:
    print(file.readlines())
