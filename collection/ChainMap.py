# This encapsulates many dictionaries into one unit

# Suppose we have two dictionaries than ChainMap help to convert them to a single list

from collections import ChainMap

a= {1:'Lsit',2:'Tuple'}
b= {3:'deque',4:'Counter'}
ab=ChainMap(a,b)
print(ab)
print(ab.get(3))
