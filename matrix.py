#AishwaryaPothula
#Learning to work with matricies using numpy

import numpy
a=numpy.array([[1,2,3,13],[4,5,6,11],[7,8,9,10],[15,0,4,0]])
b=numpy.ones((4,4))
r=numpy.zeros((4,4))

#Operations on Matrix
print(type(a))
print(a.shape)
print(a)


#Slicing
print(a[1:3,2:3])#prints 6,9

#Integer Array Indexing
print(a[[1,2,3],[0,1,2]])
'''
equivalent to slicing
'''
print([a[1,0],a[2,1],a[3,2]])

#Boolean Array Indexing
bool_idx=(a%2==0)
print(bool_idx)


    
