'''
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :

Input 1:

n = 3

s = ID

Return: [1, 3, 2]

'''
class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        low=1
        high=B
        res=[]
        for i in str(A):

            if i=='I':
                
                res.append(low)
                low+=1
                
            if i=='D':
                
                res.append(high)
                high-=1
        
        res.append(high)
        return res
