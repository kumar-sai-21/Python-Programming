# 5. Calculate avg marks of the student
# SAI KUMAR SATAPATHY
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
def avg(i):
    c=0
    t=0
    if(i['PHY']!=None):
        c=c+1
        t=t+i['PHY']
    if(i['CHEM']!=None):
        c=c+1
        t=t+i['CHEM']
    if(i['MATH']!=None):
        c=c+1
        t=t+i['MATH']
    if(c==0):
        return 0
    return float(t)/c

for i in student.keys():
    student[i]['AVG']=avg(student[i])
    
for a,b in student.items():
    print("#Average mark of", a, "is",b['AVG'])
