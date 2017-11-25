n=int(input("remove 2,3 multiples till\n"))
a=range(1,n+1)
b=a[:]
for x in a:
    if x%2==0 or x%3==0:
        b.remove(x)
print(b)
#a=list of numbers till n
#interates a list
#since we cannot operate on iterating list we create a copy
#simple b=a will not work in oython as b will point to the same memory
#making changes in a will change b too
#to make a copy in python new=original[:]
#checks for multiples of 2 or 3
#removes multiples and prints
