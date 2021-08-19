 # dict subclass that remembers the order entries were added
# A Python program to demonstrate working of deletion
# re-insertion in OrderedDict
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
	print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
	print(key, value)
