# Python Program to print Palindrome numbers from 1 to 100
# SAI KUMAR SATAPATHY

mini = int(input(" Please Enter the Minimum Value : "))
maxi = int(input(" Please Enter the Maximum Value : "))
if(mini<maxi):
    print("Palindrome Numbers between %d and %d are : " %(mini, maxi))
    for num in range(mini, maxi + 1):
        temp = num
        reverse = 0
    
        while(temp > 0):
            r = temp % 10
            reverse = (reverse * 10) + r
            temp = temp //10

        if(num == reverse):
            print(  num , end = '   ')
else:
    print("MINIMUM VALUE IS GREATER THAN MAXIMUM VALUE")
