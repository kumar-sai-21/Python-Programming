#2.Find the total factors for a given integer N.
#SAI KUMAR SATAPATHY
def find(n):
    cnt=0
    for i in range(1,n+1):
        if(n%i==0):
            #print(i)
            cnt=cnt+1
            #print(cnt)
    return(cnt)
            

n=int(input("Enter the n value   "))
no=find(n)
print("The no of factor are ",end="")
print(no)
