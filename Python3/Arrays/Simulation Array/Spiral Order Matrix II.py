'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000
Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        w=A-1
        l=0
        a=[[0 for i in range(A)] for j in range(A)]
        squr=int((A+1)/2)
        c=1
        for i in range(squr):
            for j in range(l,w+1):
                a[i][j]=c
                c+=1
            for j in range(l+1,w+1):
                a[j][w]=c
                c+=1
            for j in range(w-1,l-1,-1):
                a[w][j]=c
                c+=1
            for j in range(w-1,l,-1):
                a[j][l]=c
                c+=1
            l+=1
            w-=1
        return a
