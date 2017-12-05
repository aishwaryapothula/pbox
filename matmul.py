#Multiply Matricies also Transverse-becasue matrix be is only 1s


import numpy
a=numpy.array([[1,2,3,13],[4,5,6,11],[7,8,9,10],[15,0,4,0]])
b=numpy.ones((4,4))
r=numpy.zeros((4,4))

#Multiplication

for i in range(0,len(a)):
    for j in range(0,len(a)):
        r[i,j]=a[j,i]*b[i,j]
print(r)



