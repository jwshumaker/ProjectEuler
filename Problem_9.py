'''
Created on Apr 8, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

SOLUTION:
This is a brute force solution.
'''

import math

# Find the pythagorean triplet that produces a given integer.
def FindPythagoreanTriplet(sum):
    # Not to be boring, but let's loop through possible sequences.
    # Since a <= b < c, a < sum/3.
    for a in range(2, sum // 3 + 1):
        # Since b + c = sum - a and b < c, b must be less than (sum - a) / 2
        for b in range(a, (sum - a) // 2 + 1): 
            # Given a and b, we can compute c.           
            c = math.sqrt(a ** 2 + b ** 2)
            if a + b + c == sum:
                return a * b * c
    
    # We return -1 if no such sequence was found.
    return -1

# Again, this is thrown into a function.
print(FindPythagoreanTriplet(1000))
