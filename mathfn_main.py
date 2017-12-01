#AishwaryaPothula
#To perform math functions and first use of main

import math

def trig(deg):
    a=math.sin(deg)
    b=math.cos(deg)
    c=math.tan(deg)
    return a,b,c

def powers(base,ex):
    c=math.pow(base,ex)
    return c

def main():
    a=int(input(("Enter degrees to find sin,cos,tan functions of\n")))
    print(trig(a))
    print("Enter values to find powers")
    x=int(input("Enter base value= "))
    y=int((input("Enter exponent value= ")))
    print(powers(x,y))

if __name__=="__main__":
    main()

#A special variable __name__ is by default assigned the name of the main module running.
#We are asking the system to execute the instructions under main() only if the value of __name__ is main-which translates to asking the system to execute main only if the program is being run as a standalone.
#If the whole program is being used by another larger program,the insturctions under main() will not be executed as __name__v value will be the name of the larger program.The larger program uses the functions defined outside the main()
#Instructions in main() are usually instructions which other/larger programs will not require if they use the program as a module.Intructions under main() are usually written to test the working of functions written outside the main().
