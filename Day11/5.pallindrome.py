#palindrome words
#Sai Kumar Satapathy
import os
import open_file 
new = open("myOutFile.txt","w")   
for i in open_file.word_cls:
    if(i==i[::-1]):
        
        new.write(i+",")      #to give comma in between the words
        #new.write(i+"\n")    #to print in next line
        #new.write(i+"\t")    #for a single tab
        print (i)