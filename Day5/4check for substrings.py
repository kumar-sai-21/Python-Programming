#Find if the sub-string exists in the string without using in operator
#SAI KUMAR SATAPATHY

str1=input("enter the string")
print(str1)
str2=input("enter another string")
if str1.find(str2)!=-1:
    print("found")
else:
    print("not found")
#for i in range(0,len(str2)):
#    for j in range(0,len(str1)):
#        if str2[i]!=str1[j]:
#            str1.remove(str1[j])
#        else:
#            continue
#if str1==str2:
#    print("substring found")
#else:
#    print("substring not found")
    
            
