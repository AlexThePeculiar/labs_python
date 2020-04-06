import math as mth
import sys

def Powah (N):
    if mth.ceil(mth.log(N,2)) == mth.floor(mth.log(N,2)):
        flag = True
    else: flag = False
    return flag

if len(sys.argv) == 1:
    print("Welcome! To find whether the given number is a power of 2,",
      "please follow the instruction below.")
    while True:
        try:
            N = float(input("Enter the number to check: "))
            if N <= 0:
                print()
                print("Please, enter a valid number (greater than zero).")
            else: break
        except:
            print()
            print("Please, enter a valid number",
                      "(of float type and greater than 0)")

else:
    try:
        N = float(sys.argv[1])
    except:
        print()
        print("The entered number is invalid (not of float type).")
        quit()
    else:
        if N <= 0:
            print()
            print("The entered number is invalid",
                  "(is less than or equal to zero).")
            quit()

if Powah(N):
    print()
    print("The number {0} is indeed a power of 2.".format(N))
else:
    print()
    print("The number {0} is not a power of 2.".format(N))
    