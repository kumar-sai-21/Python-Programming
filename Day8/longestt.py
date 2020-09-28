dic={}
sentence=input("Enter the sentence ")

dic={sentence}
maxs = -1
for ele in sentence: 
    if len(ele) > maxs: 
        maxs = len(ele) 
        res = ele 
#lists={maxs = len(ele), res = ele, for ele in (sentence) if len(ele) > maxs:  }
  
print("Maximum length string is : " + res) 