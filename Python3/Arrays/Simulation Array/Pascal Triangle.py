'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        i=0
        j=0
        pas_triangle=[[0 for j in range(i+1)]for i in range(A)]
        for i in range(A):
            pas_triangle[i][0]=1
            for j in range(1,i+1):
                if j==i:
                    pas_triangle[i][j]=1
                else:
                    pas_triangle[i][j]=pas_triangle[i-1][j]+pas_triangle[i-1][j-1]
        return pas_triangle

