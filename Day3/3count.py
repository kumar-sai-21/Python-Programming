#3. Write a program that accepts a sentence and calculate the number of letters and digits.
#SAI KUMAR SATAPATHY
sen=input("Enter the Sentence  ")
l=0
d=0
for i in sen:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("The no of  Letter in the Sentence is  ", l)
print("The no of Digit in the Sentence is  ", d)
