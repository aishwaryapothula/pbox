#AishwaryaPothula
#Learning to work with matricies

import numpy
a=numpy.array([[1,2,3,13],[4,5,6,11],[7,8,9,10],[15,0,4,0]])
b=numpy.ones((4,4))
r=numpy.zeros((4,4))


print(type(a))
print(a.shape)
print(a)


'''
slicing
'''
print(a[1:3,2:3])#prints 6,9
'''
    
Multiply Matricies
'''
for i in range(0,len(a)):
    for j in range(0,len(a)):
        r[i,j]=a[j,i]*b[i,j]
print(r)
