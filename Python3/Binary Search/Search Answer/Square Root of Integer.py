'''
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
'''
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==1 or A==0:
            return A
        start = 0
        end = A
        while(start <= end):
            mid = start + (end - start)//2
            if mid*mid==A:
                return mid
            if mid*mid < A:
                start = mid + 1
            else:
                end = mid - 1
        return start-1
