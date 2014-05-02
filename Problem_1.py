'''
Created on Apr 6, 2014

@author: JWShumaker
Problem ID 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def find_multiples(a, b, max):
    multiples = 0
    #find all multiples of a, excluding those divisible by b
    #note that our range starts at 1 and goes to floor((max - 1)) + 1
    #    this insures that all multiples are evaluated, but max itself is not
    for x in range(1, ((max - 1) // a) + 1):
        if x % b:
            multiples += x * a 
            
    #now find all multiples of b, INCLUDING those divisible by a    
    for x in range(1, ((max - 1) // b) + 1):    
        multiples += x * b 
        
    return multiples

print(find_multiples(3, 5, 1000))
    
