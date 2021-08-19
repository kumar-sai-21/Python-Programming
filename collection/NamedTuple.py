# It returns a tuple with named entry which means there will be  a name
# assigned to each value in the tuple
#  using this we will not need to remember the index no to Specified element

from collections import namedtuple
a= namedtuple('Courses', 'Name,Technology')
s= a('Data Science', 'Python')
print(s)
print(s.Name, s.Technology)
