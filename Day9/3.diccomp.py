#3. Take a sentence and output a dictionary with word as the key and number of characters in the word as value
#SAI KUMAR SATAPATHY
sentence=input("Enter the Sentence ").split(" ")
word={word:len(word)for word in sentence}
print (word)