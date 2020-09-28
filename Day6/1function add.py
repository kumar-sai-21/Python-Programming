#1. Create an add function that is agnostic to number of inputs
#SAI KUMAR SATAPATHY

def addition(*args):
    s=0
    for i in args:
        s=s+i
    return s

