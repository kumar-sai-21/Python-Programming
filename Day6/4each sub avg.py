#4. Given students and their marks in following format calculate average marks for every subject
#SAI KUMAR SATAPATHY
student={'A': {'PHY': 88, 'CHEM': 71, 'MATH': 88},
'B': {'PHY': 52, 'CHEM': 99, 'MATH': 21},
'C': {'PHY': 56, 'CHEM': 59, 'MATH': 28},
'D': {'PHY': 15, 'CHEM': 61, 'MATH': 79},
'E': {'PHY': 18, 'CHEM': 61, 'MATH': 82},
'F': {'PHY': 41, 'CHEM': 70, 'MATH': 59},
'G': {'PHY': None, 'CHEM': 61, 'MATH': 54},
'H': {'PHY': 71, 'CHEM': None, 'MATH': 10},
'I': {'PHY': 65, 'CHEM': 9, 'MATH': 65},
'J': {'PHY': 69, 'CHEM': 39, 'MATH': 75},
'K': {'PHY': 92, 'CHEM': 11, 'MATH': None},
'L': {'PHY': None, 'CHEM': None, 'MATH': None}
}
p=0
c=0
m=0
c1=0
c2=0
c3=0
for i in student.values():
    for key,val in i.items():
        if(key=='PHY'):
            if(val!=None):
                p=p+int(val)
            else:
                c1=c1+1
                continue
        elif(key=='CHEM'):
            if(val!=None):
                c=c+int(val)
            else:
                c2=c2+1
                continue
        else:
            if(val!=None):
                m=m+int(val)
            else:
                c3=c3+1
                continue
print("Average mark in phy is:",p/(12-c1))
print("Average mark in chem is:",c/(12-c2))
print("Average mark in phy is:",m/(12-c3))


            
