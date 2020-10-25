'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if k is 0:
            return [1]
        elif k is 1:
            return [1,1]
            
        preveious = [1,1]
        current = []
        for i in range(1,k):
            current = [1]
            for j in range(len(preveious)-1):
                current.append(preveious[j] + preveious[j+1])
            current.append(1)
            preveious = current
        return current
