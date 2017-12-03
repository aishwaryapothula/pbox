#AishwaryaPothula
#To apply linear regression

import random
import math

x=[]
y=[]
i=1
z=0
x2=[]
xy=[]

while(i<=5):
    a=random.randint(0,101)
    b=random.randint(0,101)
    x.append(a)
    y.append(b)
    dict={"body":a,"brain":b}
    print(dict)
    i+=1
print("\n{} independent variables".format(x))
print("{} dependent variables".format(y))

while(z<len(x)):
    x2.append(x[z]**2)
    xy.append(x[z]*y[z])
    z+=1
print("\n{} x sqaures".format(x2))
print("{} xy".format(xy))

ce1=((sum(y)*sum(x2))-(sum(x)*sum(xy)))/((i*sum(x2))-(sum(x)**2))
ce2=((i*sum(xy))-(sum(x)*sum(y)))/((i*sum(x2))-(sum(x)**2))
print("\n{}".format(ce1))
print(ce2)

x0=input("enter independent value to find dependent value: ")
y0=ce1*x0+ce2
print("dependent value is: {}".format(y0))






