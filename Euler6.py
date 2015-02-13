'''
Created on Mar 4, 2014

@author: TPoole

Problem Summary:

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import sys;

def main():
    count = 0;
    sumOfSquares = 0;
    
    for i in range(1, 101):
        sumOfSquares = sumOfSquares + (i*i);
        count = count + i;
        
    count = count*count;
    
    count = count - sumOfSquares;
    print(count);
if __name__ == '__main__':
    main();
    sys.exit();