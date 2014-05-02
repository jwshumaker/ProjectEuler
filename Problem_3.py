'''
Created on Apr 7, 2014

@author: JWShumaker
ProjectEuler.net
Problem ID 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math



# Test p to see if it is prime
def IsPrime(p):
    # We only need to check values between 2 and the square root of p.
    for x in range(2, math.floor(math.sqrt(p)) + 1):
        if not p % x:
            return False
    # If p was not divisible, then it must be prime
    return True

# Find the largest prime factor of a
def LargestPrime(a):
    # Let's assume that a is prime, hence it is it's own largest factor
    # If we find another prime that divides a, a must not be prime
    largest = a
    
    # Loop through all possible factors between 2 and the square root of a
    for x in range(2, math.floor(math.sqrt(a)) + 1):
        # If x divides a and is prime, set it as our new largest prime factor
        if not a % x and IsPrime(x):
            largest = x
    
    return largest

print(LargestPrime(600851475143))
