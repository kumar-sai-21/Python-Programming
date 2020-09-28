#5. Given a list of strings find the longest common prefix for them
#SAI KUMAR SATAPATHY
my_list = input('Enter the strings sparated by space: ').split()

if not my_list:
    print('')

prefix = my_list[0]       
for word in my_list:
    if len(prefix) > len(word):
        prefix,word = word,prefix    

    while len(prefix) > 0:
        if word[:len(prefix)] == prefix:
            break
        else:
            prefix = prefix[:-1]

print(prefix)

        
