'''
Created on Apr 8, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 6
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
 and the square of the sum is 3025 - 385 = 2640.
 
Find the difference between the sum of the squares of the first one hundred natural
 numbers and the square of the sum.

SOLUTION:
Let's just brute force this.  To be a bit smarter, we will keep a running sum of squares
 and current range.
'''

# To make this just a bit more applicable, our algorithm will work for any range.
def DifferenceOfSquares(min, max, sums = 0, sum_of_squares = 0, square_of_sums = 0):
    # Loop over our range while updating sums and sum_of_squares.
    for x in range(min, max + 1):
        sums += x
        sum_of_squares += x ** 2
    
    # Now find the square_of_sums.
    square_of_sums = sums ** 2

    # Then return the difference.  Note that square_of_sums > sum_of_squares. Always.
    return square_of_sums - sum_of_squares

# Again, let's call a function.
print(DifferenceOfSquares(1, 100))
