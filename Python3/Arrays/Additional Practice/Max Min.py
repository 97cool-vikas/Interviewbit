'''
Problem Description

Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the sum Maximum and Minimum element in the given array.



Example Input
Input 1:

 A = [-2, 1, -4, 5, 3]
Input 2:

 A = [1, 3, 4, 1]


Example Output
Output 1:

 1
Output 2:

 5


Example Explanation
Explanation 1:

 Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1. 
Explanation 2:

 Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.
'''
def getMinMax(low, high, A): 
    arr_max = A[low] 
    arr_min = A[low] 
      
    # If there is only one element  
    if low == high: 
        arr_max = A[low] 
        arr_min = A[low] 
        return (arr_max, arr_min) 
          
    # If there is only two element 
    elif high == low + 1: 
        if A[low] > A[high]: 
            arr_max = A[low] 
            arr_min = A[high] 
        else: 
            arr_max = A[high] 
            arr_min = A[low] 
        return (arr_max, arr_min) 
    else: 
          
        # If there are more than 2 elements 
        mid = int((low + high) / 2) 
        arr_max1, arr_min1 = getMinMax(low, mid, A) 
        arr_max2, arr_min2 = getMinMax(mid + 1, high, A) 
  
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxi, mini  = getMinMax(0, len(A) -1, A)
        ans = maxi + mini
        return ans
