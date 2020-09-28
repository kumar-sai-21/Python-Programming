#1.CWrite a program to solve a classic ancient Chinese puzzle: We count 35 heads and
#94 legs among the chickens and rabbits in a farm. How many rabbits and how many
#chickens do we have?
#SAI KUMAR SATAPATHY
def solve(head,leg):
    #head=35
    #leg=94
    for i in range(head+1):
        j=head-i
        if (2*i)+(4*j)==leg:
            return i,j
    return "nosolutions"
head=int(input("Enter the no of head  "))
leg= int(input("Enter the no of legs  "))
print("The no of chiken and Rabbit are " ,end='')
print (solve(head,leg))