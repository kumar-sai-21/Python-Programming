#3. Create a custom exception
#sai kumar satapathy
class myerror(BaseException):
    pass
def main():
    str1=input("enter the name")
    if(len(str1)<10):
        #try:
            raise myerror(str1)
        #except myerror:
        #print("enter name having length greater than 10")
    return "THANK YOU"
print(main())
