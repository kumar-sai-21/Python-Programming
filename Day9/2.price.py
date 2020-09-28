#2. Take two list of numbers of products quantities and prices and calculate total price.
#SAI KUMAR SATAPATHY
t=0
quan = input("Enter the quantity with space ").split(' ')
cost =input("Enter the cost  ").split(' ')
x=len(cost)
#for i in  range(0, x):
#t= [(t+(int(quan[i])*int(cost[i])))  for i in  range(0, x)]
t= [(int(quan[i])*int(cost[i]))  for i in  range(0, x)]
print(t)
total= sum(t)
print(total)