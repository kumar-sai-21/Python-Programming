#Print the longest palindrome in sowpods.txt
#SAI KUMAR SATAPATHY
def pal(sow_list):
    max_=0
    for item in sow_list:
        if item==item[::-1]:
            if len(item)>max_:
                max_=len(item)
                i=item
    return i
sow=open("sowpods.txt")
sow_list={word.strip() for word in sow.readlines()}
sow.close()
print("The longest palindrome in sonnets file is: ",pal(sow_list))


