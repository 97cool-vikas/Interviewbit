'''
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.



Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.
Constraints:

1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
 
 '''
 class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)  
        n = len(A[0])  
        zero_rows_element = set()
        zero_cols_element = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
 
                    zero_rows_element.add(i)
                    zero_cols_element.add(j)
 
        for i in range(m):
            if i in zero_rows_element:
                A[i] = [0] * n
        for j in range(n):
            if j in zero_cols_element:
                for cell in range(m):
                    A[cell][j] = 0
 
        return A
