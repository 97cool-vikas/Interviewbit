'''
Problem Description

Given a 2D integer matrix A of size N x N find a B x B submatrix where B<= N and B>= 1, such that sum of all the elements in submatrix is maximum.



Problem Constraints
1 <= N <= 103.

1 <= B <= N

-102 <= A[i][j] <= 102.



Input Format
First arguement is an 2D integer matrix A.

Second argument is an integer B.



Output Format
Return a single integer denoting the maximum sum of submatrix of size B x B.



Example Input
Input 1:

 A = [
        [1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2]
        [3, 8, 6, 7, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5, 5]
     ]
 B = 3
Input 2:

 A = [
        [2, 2]
        [2, 2]
    ]
 B = 2


Example Output
Output 1:

 48
Output 2:

 8


Example Explanation
Explanation 1:

    Maximum sum 3 x 3 matrix is
    8 6 7
    4 4 4
    5 5 5
    Sum = 48
Explanation 2:

 Maximum sum 2 x 2 matrix is
  2 2
  2 2
  Sum = 8
'''

def valid(i, j, n):
    return (i>=0 and i<n and j>=0 and j<n)
    
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        if n==0:
            return 0
        ans=-10000000
        for i in range(n):
            for j in range(n):
                if valid(i-1, j, n):
                    A[i][j]+=A[i-1][j]
                if valid(i, j-1, n):
                    A[i][j]+=A[i][j-1]
                if valid(i-1, j-1, n):
                    A[i][j]-=A[i-1][j-1]
        
        for i in range(n):
            for j in range(n):
                if i==B-1 and j==B-1:
                    ans=max(ans, A[i][j])
                if i==B-1 and j-B>=0:
                    curarea=A[i][j]-A[i][j-B]
                    ans=max(ans, curarea)
                if j==B-1 and i-B>=0:
                    curarea=A[i][j]-A[i-B][j]
                    ans=max(ans, curarea)
                if valid(i-B, j-B, n):
                    curarea=A[i][j]-A[i-B][j]-A[i][j-B]+A[i-B][j-B]
                    ans=max(ans, curarea)
        return ans
 
