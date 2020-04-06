import math as mth
import sys

def Fibonacci(n):
    phi = (1 + mth.sqrt(5))/2
    Fibb = mth.floor((phi**n-(-phi)**(-n))/(2*phi - 1))
    return Fibb

def Leonardo(n):
    Leo = 2*Fibonacci(n+1)-1
    return Leo
    
def Ending(n):
    ends = ["st","nd","rd"]
    if n%10 in range(1,4) and int(n/10)%10 != 1:
        E = ends[n%10-1]
    else: E = "th"
    return E

if len(sys.argv) == 1:
    print("Welcome! To find the n-th Leonardo number,",
      "please follow the instructions below.")
    while True:
        try:
            N = int(input("Enter the number N for the N-th Leonardo number: "))
            if N < 0:
                print("Please, enter a valid number (greater than zero).")
            else: break
        except:
            print()
            print("Please, enter a valid number (of integer type).")
            
else:
    try:
        N = int(sys.argv[1])
    except:
        print()
        print("The entered number is invalid (not of integer type).")
        quit()
    else:
        if N < 0:
            print()
            print("The entered number is invalid (less than zero).")
            quit()
print()
print("The {0}-{1} Leonardo number is {2}.".format(N, Ending(N), Leonardo(N)))