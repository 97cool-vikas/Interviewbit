'''
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4.
'''
import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        res=False
        i=2
        while i*i<=A:
            if(abs(math.log(A, i)-int(math.log(A, i))) < 0.000001):
                res=True
            i+=1
        return int(res)
