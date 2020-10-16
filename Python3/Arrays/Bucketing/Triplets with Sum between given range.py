'''
Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.

Example:

Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

You should return 1

as

0.6+0.7+0.4=1.7

1<1.7<2

Hence, the output is 1.

O(n) solution is expected.

Note: You can assume the numbers in strings don’t overflow the primitive data type and there are no leading zeroes in numbers. Extra memory usage is allowed

'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        t=[0]*len(A)
        for i in range(len(A)):
            t[i]=float(A[i])
        t.sort()
        for i in range(len(A)):
            j=i+1
            k=j+1
            if(k<len(A) and j<len(A)):
                    a=t[i]+t[j]+t[k]
                    if (a>2):
                        a=t[k]+t[0]+t[1]
                    if(a>1 and a<2):
                        return 1
        return 0  
