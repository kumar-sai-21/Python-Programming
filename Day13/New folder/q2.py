#Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the input string is valid

def check(string):
    stack=[]
    for char in string:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char=='(' and char!=")":
                return False
            if current_char=='{' and char!="}":
                return False
            if current_char=='[' and char != "]":
                return False
    if stack:
        return False
    return True

string=input("Enter the string: ")
if check(string):
    print("Valid")
else:
    print("Not Valid")
