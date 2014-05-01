'''
Created on Apr 8, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
 6th prime is 13.

What is the 10 001st prime number?

SOLUTION:
It would be nice to use the Sieve of Erotosthenes, however it is hard to identify an
 upper limit for our sieve.  So, let's try a brute force approach.
'''

import math

# Our primality test.
def IsPrime(p):
    # Let's see if p is composite.
    for x in range(2, math.floor(math.sqrt(p)) + 1):
        if not p % x:
            return False
        
    # Since p is not composite, it must be prime.
    return True

# A simple method to find the Nth prime.
def NthPrime(N):
    primes_found = 0
    last_prime, current = 1, 1
    
    # Loop until we find the Nth prime.
    while (primes_found < N):
        current += 1
        
        if IsPrime(current):
            last_prime = current
            primes_found += 1
        
    return last_prime

# Our function call.
print(NthPrime(10001))
