#AishwaryaPothula
#To list integers

n= int(input("Enter a number to divide: "))

list = list(range(1,n+1))

divisors = []

for num in list:
    if n % num == 0:
        divisors.append(num)

print(divisors)
