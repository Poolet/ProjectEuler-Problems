'''
Created on Mar 4, 2014

@author: TPoole
'''

'''
Problem Summary:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''
import sys

def main():
    a = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            a = a + i;
    print(a);
    
if __name__ == '__main__':
    main()
    sys.exit()