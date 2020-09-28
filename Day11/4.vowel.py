#find the word which contain all the vowels
#sai kumar
import os
import open_file
for word in open_file.word_cls:
    if ('A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word):
        print(word)