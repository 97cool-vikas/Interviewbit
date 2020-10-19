'''
Problem Description

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].



Input Format
First and only argument is an integer array A.



Output Format
Return an integer denoting the maximum value of j - i;



Example Input
Input 1:

 A = [3, 5, 4, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Maximum value occurs for pair (3, 4).
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A:
            return -1
        N = len(A)
        leftMin = [0]* N
        rightMax = [0] * N
        leftMin[0] = A[0]
        for i in range(1, N):
            leftMin[i] = min(leftMin[i-1], A[i])
        rightMax[N-1] = A[N-1]
        for i in range(N-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], A[i])
        
        minI = maxJ = 0
        currMax = 0
        while minI < N and maxJ < N:
            if leftMin[minI] <= rightMax[maxJ]:
                currMax = max(currMax, maxJ - minI)
                maxJ += 1
            else:
                minI += 1
        
        return currMax
