# Couter is aa sub calss that is used to count hashable object
# It Implicitly creates a hash table of an iterable when invoked

from collections import Counter
a=[1,1,1,2,5,2,2,4,4,4,6,66,6,6,12,8,8,7,55,7,66,6,34,5,4,34]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
