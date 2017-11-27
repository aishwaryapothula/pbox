#AishwaryaPothula
#To print a dictionary with sqaure upto the number given

def dict_sq(num):
    n=range(1,num+1)
    a={i:i**2 for i in n}
    return a
num=input("list squares untill\n")
z=dict_sq(num)
print(z)
print(type(z))

#defining a funtion, takes one argument
#n is a list of all numbers till specified number
#creating a dictionary{keyi:valuei^2}using list comprehension.Iterates over n
#returns value of a when function is called
