'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False
'''
import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A<0:
            return 0
        if A == 0:
            return 1
        
        n = int(math.log10(A)+1)
        digits = n
        
        while A > 0:
            last = A%10
            first = A//(10**(digits-1))
            if last != first:
                return 0
            A = A%(10**(digits-1))
            A = A//10
            digits -= 2
        
        return 1
