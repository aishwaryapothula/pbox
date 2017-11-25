
#aishwaryapothula
#To list all prime numbers between specified range

lower=input("prime numbers starting from \n")
higher=input("all prime numbers till\n")
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

#ex:given range 3 to 10
# for num in range(3,11)
#since num is >3
#interation of i starts
#3%2!=0 so second for loop iterates again
#3%3==0 condition met break-so comes out of second for loop
#iteration of num-num++
#4 then enters second loop and so on

