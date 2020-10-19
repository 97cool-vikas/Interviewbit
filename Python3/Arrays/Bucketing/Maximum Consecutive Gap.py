'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5 
Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = list(A)
        A.sort()
        ans = 0
        if len(A)<2:
            return 0
        for j in range(len(A)-1):
            if(A[j+1]-A[j]>ans):
                ans = A[j+1]-A[j]
        
        return ans
