#1.Join two sorted lists such that the final list is also sorted
#SAI KUMAR SATAPATHY

li1=input("Enter numbers in the list separated by space").split()
li1=[int(i) for i in li1]
li1.sort()
li2=input("Enter numbers in the list separated by space").split()
li2=[int(i) for i in li2]
li2.sort()
c=[]
i, j = 0, 0
  
while i<len(li1) and j<len(li2): 
    if li1[i]<li2[j]: 
      c.append(li1[i]) 
      i+=1
    elif li1[i]>li2[j]: 
      c.append(li2[j]) 
      j+=1
    else:
        c.append(li1[i])
        i+=1
        j+=1
c=c+li1[i:]+li2[j:]
print(c)
