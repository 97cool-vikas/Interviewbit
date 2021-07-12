'''
Problem Description

Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.


Problem Constraints
3 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A containing N integers.



Output Format
Return 1 if there exist a element that is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it else return 0.



Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 A[4] = 6 is the element we are looking for.
 All elements on left of A[4] are smaller than it and all elements on right are greater.
Explanation 2:

 No such element exits.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        min_a = [0]*len(A)
        max_a = [0]*len(A)
        maxa = A[0]
        mina = A[-1]
        n= len(A)
        for i in range(len(A)):
            if A[i]>maxa:
                max_a[i] = A[i]
                maxa= A[i]
            elif A[i]<maxa:
                max_a[i] = maxa
            else:
                max_a[i] = None
                
            if A[n-i-1] < mina:
                min_a[n-i-1] = A[n-i-1]
                mina = A[n-i-1]
            elif A[n-i-1]>mina:
                A[n-i-1] = mina
            else:
                min_a[n-i-1]=None
        for i in range(1,n-1):
            if A[i]==max_a[i] and A[i]==min_a[i]:
                return 1
        return 0

      
