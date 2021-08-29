#wap to check a number is a prim number or not
x=int(input("Enter the  number"))
if(x>1):
    for i in range(2,x):
        if (x%i==0):
            break;
        else:
            print("this is prime")
#if(cnt==2):
  #  print("IT IS A PRIME NUMBER")
#else:
  #  print("IT IS NOT A PRIME NUMBERs")
    
    
