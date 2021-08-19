# This is a optimised list to perform insertion and deletion operation

from collections import deque

a = ['s', 'a', 'i', 'k', 'u', 'm', 'a', 'r']
d = deque(a)
print(d)
d.append('Python')
print(d)
d.appendleft('Java')
print(d)
d.reverse()
print(d)
d.pop()
print(d)
