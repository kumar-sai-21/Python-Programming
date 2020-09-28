#3.Write a program that accepts sequence of lines as input and prints the lines after
#making all characters in the sentence capitalized. Suppose the following input is
#supplied to the program
#SAI KUMAR SATAPATHY

lines=[]
print("Enter the string to capitalize and double enter to get output  ")
while True:
    s =input()
    if s:
        lines.append(s.upper())
    else:
        break;

for s in lines:
    print (s)
