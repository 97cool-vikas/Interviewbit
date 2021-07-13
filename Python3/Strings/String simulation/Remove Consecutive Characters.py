'''
Problem Description

Given a string A and integer B, remove all consecutive same characters that have length exactly B.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= |A|



Input Format
First Argument is string A.

Second argument is integer B.



Output Format
Return a string after doing the removals.



Example Input
Input 1:

A = "aabcd"
B = 2
Input 2:

A = "aabbccd"
B = 2


Example Output
Output 1:

 "bcd"
Output 2:

 "d"


Example Explanation
Explanation 1:

 "aa" had length 2.
Explanation 2:

 "aa", "bb" and "cc" had length of 2.
'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        a = len(A)
        i = 0
        d = "" #d is used here for the remaining characters
        c = A # cis used here for updating the sliced material
        while i < len(A):
            if(i == len(A) - B and A[i:i + B] == A[i] * B): #last possible case such that if B=2 and A=bcdaa,
                c = A[i + B:]
                i += B
            elif(i > len(A) - B): #consider aabcd
                d += A[i]
                i += 1
            elif(A[i:i + B] == A[i] * B): #inbetween
                c = A[i + B:]
                i += B
            else: #inbetween single characters
                d += A[i]
                i += 1
        return d
