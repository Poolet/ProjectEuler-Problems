'''
Created on Mar 4, 2014

@author: TPoole

Problem Summary:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import sys;
def findAnswer():
    i = 1;
    while(i%1 != 0 or i%2 != 0 or i%3 != 0 or i%4 != 0 or i%5 != 0 or i%6 != 0 or i%7 != 0 or i%8 != 0 or i%9 != 0 or i%10 != 0 or i%11 != 0 or i%12 != 0 or i%13 != 0 or i%14 != 0 or i%15 != 0 or i%16 != 0 or i%17 != 0 or i%18 != 0 or i%19 != 0 or i%20 != 0):
            i = i + 1;
    return i;
        

def main():
    answer = findAnswer();
    print(answer);

if __name__ == '__main__':
    main();
    sys.exit();