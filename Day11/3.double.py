#find the word which is non- repitive

import os
import string
import open_file
for alpha in string.ascii_uppercase:
    flag=True
    for word in open_file.word_cls:
        if alpha*2 in word:
            flag =False
            break
    if(flag):
        print(alpha)