#aishwaryapothula
#Guess the correct number

import random
a=random.randint(1,21)
counter=0
num=int(input("guess the number. You have 6 chances\n"))
while(counter<6):
    if(num<a):
        num=int(input("Guess higher\n"))
        counter+=1
    elif(num>a):
        num=int(input("guess lower\n"))
        counter+=1
    elif(num==a):
        print("yay!you guessed it right")
        counter+=1
        break
if(counter==6):
    print("The number is {}.Better luck next time".format(a))

#importing random module from python
#random.randint selects a random integer from the given range
#using variable counter to count number of chances
#taking guesses and checking conditions
#if it is not the right number the loop goes on for 6 times otherwise break from loop;increments counter
#checks for counter value and if it exceeds 6 chances game ends
