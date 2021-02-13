'''
Problem Description

Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)



Problem Constraints
1 <= N <= 106

1 <= A[i], B <= 109



Input Format
First agument is an integer array A of size N.

Second argument is an integer B.



Output Format
Return an integer denoting the number of elements which are less than or equal to B.



Example Input
Input 1:

 A = [1, 3, 4, 4, 6]
 B = 4
Input 2:

 A = [1, 2, 5, 5]
 B = 3


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 Elements (1, 3, 4, 4) are less than or equal to 4.
Explanation 2:

 Elements (1, 2) are less than or equal to 3.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        left = 0
        right = n - 1
      
        count = 0
      
        while (left <= right):  
            mid = int((right + left) / 2) 
      
            # Check if middle element is less than or equal to B
            if (A[mid] <= B):  
      
                # At least (mid + 1) elements are there whose values are less than or equal to key 
                count = mid + 1
                left = mid + 1
              
            # If B is smaller, ignore right half 
            else: 
                right = mid - 1
          
        return count 
