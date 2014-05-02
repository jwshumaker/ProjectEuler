'''
Created on Apr 7, 2014

@author: spiff
ProjectEuler.net
Problem ID 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Test a given integer to see if it is a palindrome
def IsPalindrome(p):
    # Create an iterable list of digits from p
    digits = str(p)
    
    # Now we just return a comparison of the digits to the reversed digits
    # Note that digits[::-1] works because the iterable syntax is [start stop step]
    return digits == digits[::-1]

# Find the largest palindrome product for integers of length a and b
def LargestPalinProd(a, b, largest = 0):
    # Step over all digits of length a
    for x in range(10 ** (a - 1), 10 ** a):
        # By declaring current here, we also reset it for each iteration
        current = 0
        
        # Step over all digits of length b, starting from x
        for y in range(x, 10 ** b):
            # If a * b is a palindrome, it is the largest we've seen for this x
            if IsPalindrome(x * y):
                current = x * y   
        
        # Compare the largest palindrome from the last iteration to the current
        if current > largest:
            largest = current  
            
    return largest
                




# Call a function that takes two integers representing the number of digits
#     and finds the largest palindrome product produced by integers of that length
print(LargestPalinProd(3, 3))
