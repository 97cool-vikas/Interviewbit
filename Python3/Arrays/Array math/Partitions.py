'''
Problem Description

You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])



Problem Constraints
1 <= A <= 105

-109 <= B[i] <= 109



Input Format
First argument is an integer A.

Second argument is an 1D integer array B of size A.



Output Format
Return a single integer denoting the number of ways to split the array B into three parts with the same sum.



Example Input
Input 1:

 A = 5
 B = [1, 2, 3, 0, 3]
Input 2:

 A = 4
 B = [0, 1, -1, 0]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 There are no 2 ways to make partitions -
 1. (1,2)+(3)+(0,3).
 2. (1,2)+(3,0)+(3).
Explanation 2:

 There is only 1 way to make partition -
 1. (0)+(-1,1)+(0).
 
 '''
 class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        tot = sum(B)
        if tot % 3 == 0:
            target = tot // 3
        else:
            return 0
        res = 0
        f = 0
        s = 0
        for i in range(A - 1):
            s += B[i]
    
            if s == 2 * target:
                res += f
            if s == target:
                f += 1
        return res