#this will import the .txt file
#sai kumar satapathy

import os
file=open("sowpods.txt")
my_word=file.readlines()
word_cls=[word.strip() for word in my_word]
file.close()

