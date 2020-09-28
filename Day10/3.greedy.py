#Items = (value, weight)
#Items = [(60, 10), (100, 20), (120, 30)]
#capacity = 50
def out(l,bag):
    cont=0
    for i in l:
        weight=i[1]
        #print(weight)
        value=i[0]
        #print("value=",value)
        if(weight<=bag):
            bag=bag-weight
            #print("bag",bag)
            cont=cont+value
            #print("cont",cont)
        else :
            weight=i[2]
            #print("weingt",weight)
            cont=cont+(weight*bag)
            #print(cont)
    print(cont)
x=input("Enter values :").split()
#print(x)
y=input("Enter weight :").split()
#print(y)
l=[(int(x[i]),int(y[i]),int(x[i])/int(y[i]))for i in range (len(x))]
#print(l)
ln=[(int(x[j]),int(y[j])) for j in range (len(x))]
ln=sorted(ln)
print(ln)
bag=int(input("Enter capacity of the bag :"))
out(l,bag)
    
        

