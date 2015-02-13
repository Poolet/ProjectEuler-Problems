'''
Created on Mar 4, 2014

@author: TPoole

Problem Summary:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import sys;

def main():
    x = 600851475143;
    lpf = 2;
    while (x > lpf):
        if (x%lpf==0):
            x = x/lpf
            lpf = 2
        else:
            lpf+=1;
    print("Largest Prime Factor: %d" % (lpf));
if __name__ == '__main__':
    main();
    sys.exit();