'''
Created on Apr 8, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to
     10 without any remainder.
     
    What is the smallest positive number that is evenly divisible by all of the
     numbers from 1 to 20?
    
Solution
    Note that this is a restatement asking for the Least Common Multiple of a range.
    So, our solution will find the prime factorization of each integer in the range.
    After, we will evaluate these prime factorizations to produce a number equal to
    the product of each unique prime with it's HIGHEST exponent.
'''

import math

# We create a dictionary of primes and exponents.
primes = {}

# Finds the prime factorization of number.  If the prime factorization contains
#    a prime with a greater exponent than stored in our dictionary primes, we
#    update appropriately.
def PrimeFactorization(number):
    for key in primes:
        temp_exponent = 0
        while (not number % key):
            number /= key
            temp_exponent += 1
            
        if temp_exponent > primes[key]:
            primes[key] = temp_exponent 

# Let's just create a list of all prime numbers less than max.
# To do this, we'll use the Sieve of Eratosthenes
def FindPrimes(max):
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
    for x in range(2, len(sieve)):
        if sieve[x]:
            primes[x] = 0
            
# Given a min and max integer value, assuming min > max, return the LCM.
def RangeLCM(min, max, LCM = 1):
    # First we need a dictionary of primes less than or equal to max.
    FindPrimes(max)
    
    # Next, let's loop through our range add is prime factorization info
    #    to our dictionary primes
    for x in range(min, max + 1):
        PrimeFactorization(x)
        
    # Now we build our LCM
    for key in primes:
        LCM *= key ** primes[key]
        
    return LCM

# Give our method RangeLCM a positive integer range.  Min first, max next.
print(RangeLCM(1, 20))
