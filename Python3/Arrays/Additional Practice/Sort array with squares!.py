'''
Problem Description

Given a sorted array A containing N integers both positive and negative.

You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

1.Try to this in O(N) time.


Problem Constraints
1 <= N <= 105.

-103 <= A[i] <= 103



Input Format
First and only argument is an integer array A.



Output Format
Return a integer array as described in the problem above.



Example Input
Input 1:

 A = [-6, -3, -1, 2, 4, 5]
Input 2:

 A = [-5, -4, -2, 0, 1]


Example Output
Output 1:

 [1, 4, 9, 16, 25, 36]
Output 2:

 [0, 1, 4, 16, 25]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
       
        n =len(A)
        i=0
        j=n-1
        res=[]
        while i<=j:
            if A[i]*A[i] >=A[j]*A[j]:
                res.append(A[i]*A[i])
                i+=1
            else:
              res.append(A[j]*A[j])
              j-=1
        
        return res[::-1]

