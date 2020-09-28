#Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the input string is valid

def check(string):
    stringlis=[]
    for char in string:
        if char in ["(", "{", "["]:
            stringlis.append(char)
        else:
            if not stringlis:
                return False
            current_char=stringlis.pop()
            if current_char=='(' and char!=")":
                return False
            if current_char=='{' and char!="}":
                return False
            if current_char=='[' and char != "]":
                return False
    if stringlis:
        return False
    return True

string=input("Enter the string: ")
if check(string):
    print("Valid")
else:
    print("Not Valid")

