'''
Created on Apr 8, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

SOLUTION:
Since we are given an upper bound on the largest prime, we will use the Sieve of
 Erotosthenes from Problem ID 5.
'''

import math

# Let's just create a list of all prime numbers less than max.
# To do this, we'll use the Sieve of Eratosthenes
def SumOfPrimes(max):
    product = 0
    
    # Let's create a container for our sieve.
    # We begin by assuming that all numbers are prime.
    # Note that our sieve technically identifies 0 and 1 as prime.
    sieve = [True] * (max + 1)
    
    # Now we use the Sieve of Eratosthenes to rule out composite numbers.
    # We begin with 2 and check all numbers up to the square root of max.
    for x in range(2, math.floor(math.sqrt(max)) + 1):
        # There is no need to check numbers less than x, so we find all
        #    products with factors x and y >= x.
        for y in range(x, (max // x) + 1):
            # Any number x * y is by definition a composite number. 
            sieve[(x * y)] = False
    
    # Now we check out sieve to see what prime numbers came up.
    for prime in range(2, len(sieve)):
        if sieve[prime]:
            product += prime
    
    return product

# Our modular function call.
print(SumOfPrimes(2000000))
