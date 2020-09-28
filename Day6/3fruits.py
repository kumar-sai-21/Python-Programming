#3. Given a list of products, print out the name of all the products with a price higher than 10
#SAI KUMAR SATAPATHY
d=[{'name':'orange','price':20},{'name':'apple','price':8},{'name':'banana','price':10},{'name':'kiwi','price':30}]
print("price greater than 10 are:")
for i in d:
    if(i['price']>10):
        print(i['name'])
   
        
