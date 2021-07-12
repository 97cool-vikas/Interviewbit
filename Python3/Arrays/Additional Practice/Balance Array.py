'''
Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the count of special elements.



Example Input
Input 1:

 A = [2, 1, 6, 4]
Input 2:

 A = [5, 5, 2, 5, 8]


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 After deleting 1 from array : {2,6,4}
    (2+4) = (6)
 Hence 1 is the only special element, so count is 1
Explanation 2:

 If we delete A[0] or A[1] , array will be balanced
    (5+5) = (2+8)
 So A[0] and A[1] are special elements, so count is 2.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        odd = 0
        even = 0
        leftOdd = [0] * n
        rightOdd = [0] * n
        leftEven = [0] * n
        rightEven = [0] * n
        for i in range(n):
            leftOdd[i] = odd
            leftEven[i] = even
            if(i%2 == 0):
                even += A[i]
            else:
                odd += A[i]
        
        odd = 0
        even = 0
        for i in range(n-1, -1, -1):
            rightOdd[i] = odd
            rightEven[i] = even
            if(i%2 == 0):
                even += A[i]
            else:
                odd += A[i]
        
        ans = 0
        for i in range(n):
            if(leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]):
                ans += 1
            
        return ans
      
      
