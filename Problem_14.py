'''
Created on Apr 12, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 14
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10
 terms. Although it has not been proved yet (Collatz Problem), it is thought that
  all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution:
Iterate through the natural numbers, computing the sequence length for each number.
 Record, in a dictionary, each number paired with it's sequence length.  While
 computing sequence lengths, look up each term to see if it has been seen before.
 If it has, append the known length to the length currently being constructed and
 terminate the current iteration. After our loop terminates, scan through the
 dictionary for the largest chain length and return it's key.
'''

class CollatzNumbers:
    def __init__(self):
        self.collatz_database = {1:0}
        
    def insert(self, number, chain_length):
        self.collatz_database[number] = chain_length
        
    def find_key(self, value):        
        return list(self.collatz_database.keys())[list(self.collatz_database.values()).index(value)]
    
    def lookup(self, number):
        if number in self.collatz_database:
            return self.collatz_database[number]
        else:            
            return -1
    
    def next(self, number):
        if number % 2:
            return 3 * number + 1
        else:
            return number // 2

# Given a limit, computes the integer with the longest Collatz chain length.
def CollatzChainLength(limit):
    collatz_database = CollatzNumbers()
    max_chain_length = 0
    
    # Iterate through the natural numbers starting at 2.
    for i in range(2, limit):
        number = i
        collatz_chain = []
        
        # If we haven't seen this number before, expand it's chain until we find a term
        #     that we've seen before.
        while collatz_database.lookup(number) < 0:            
            collatz_chain.append(number)
            number = collatz_database.next(number) 
        
        # We know the next term after what is contained in collatz_chain, and it's 
        #     sequence length is this.
        sequence_remainder = collatz_database.lookup(number)
                
        # Remove terms, starting at the end, from collatz_chain and record them.
        while collatz_chain:
            temp = collatz_chain.pop()
            sequence_remainder += 1
            collatz_database.insert(temp, sequence_remainder)
            max_chain_length = max(max_chain_length, sequence_remainder)
            
    return collatz_database.find_key(max_chain_length)    


# The function call.
print(CollatzChainLength(1000000))
