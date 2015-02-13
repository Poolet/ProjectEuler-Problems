'''
Created on Mar 4, 2014

@author: TPoole

Problem Summary:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
import sys;

def main():
    x = [];
    b = 0;
    answer = 0;
    for i in range(100,1000):
        for j in range(100, 1000):
            b = i*j;
            if str(b) == str(b)[::-1]:
                x.append(b);
    for i in x:
        if answer <= i:
            answer = i;
    print(answer);
        
if __name__ == '__main__':
    main();
    sys.exit();