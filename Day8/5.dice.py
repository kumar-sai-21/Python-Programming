#5. Assume a fair dice roll using a similar random integer generation code above roll for
#500 times and print the number of times 1 to 6 has appeared
#SAI KUMAR SATAPATHY
import random
cnt={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(0,501):
    roll=random.randint(1,6)
    cnt[roll]+=1
for key,value in cnt.items():
    print(key,": ",value)
