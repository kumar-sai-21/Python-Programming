#4. Run the code below to generate a matrix
#SAI KUMAR SATAPATHY
table = [list("abcd"),list("efgh"),list("ijkl")]
cha=input("ENter the target character ")
x=len(table)
for i in range(x):
    #print(table[i])
    y=len(table[i])
    for j in range(y):
        if(cha==table[i][j]):
            print(i+1,j+1)
    #if cha not in table:
    #    print("character not in the table")
