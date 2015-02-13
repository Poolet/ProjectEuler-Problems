'''
Created on Mar 5, 2014

@author: TPoole

Problem Summary:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import sys;

def getPrimes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def main():
    primes = getPrimes(2000000);
    
    answer = sum(primes);
    print(answer);
if __name__ == '__main__':
    main();
    sys.exit();