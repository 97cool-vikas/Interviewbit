'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
'''
import math
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        x=[e for e in A]
        x.sort()
        i=0
        r=0
        while x:
            r=r+(x.index(A[i])*math.factorial(len(x)-1))
            x.remove(A[i])
            i=i+1
        return (r+1)%1000003
