'''
Problem Description

Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.



**Problem Constraints**
1 <= A <= 10000



**Input Format**
First and only argumment is integer A.



**Output Format**
Return an integer, the answer to the problem.



**Example Input**
Input 1:

 A = 4
Input 2:

 A = 5


**Example Output**
Output 1:

 0
Output 2:

 1


**Example Explanation**
Explanation 1:

 4! = 24
Explanation 2:

 5! = 120
'''
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        if A < 5: return 0
        power = 1
        zeros = 0
        while pow(5, power) <= A:
            zeros += A//pow(5, power)
            power += 1
        return zeros
