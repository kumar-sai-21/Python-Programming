#4. Consider a sorted sequence of number with following pattern 2^i × 3^j × 5^k
#Approach: Take input N from the user and output the Nth number in the sequence
#SAI KUMAR SATAPATHY
n=int(input("Enter the Number"))
list=[1]
i=1
while i>0:
    if((i%2==0 or i%3==0 or i%5==0)and (i%7!=0) ):
        k=i
        list.append(k)
        
        if(len(list)==n):
            print("list is:",list)
            print("Nth Number is:",list[len(list)-1])
            x=int(input("ENter the nth position you want "))
            print("The nth position is  ", end=" ")
            print(list[x-1])
            break
    i+=1
#print(len(list))
