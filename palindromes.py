#AishwaryaPothula
#To find out whether a word is a palindrome

a=raw_input("enter a word\n") #input if executing in python2
b=a[::-1]
if a==b:
    print("is a palindrome")
else:
    print("is not a palindrome")

#takes a word as input. Use raw_input to consider entered input as string if running in python2
#a[::-1] slices the string in the reverse order
