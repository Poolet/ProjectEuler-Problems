'''
Created on Mar 5, 2014

@author: TPoole

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import sys;
import math;

def isPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True

def main():
    i = 0
    num = 2
    toFind = 10001
    while i < toFind:
        if isPrime(num):
            i = i + 1
            if i == toFind:
                print(num);
        num = num + 1

if __name__ == '__main__':
    main();
    sys.exit();