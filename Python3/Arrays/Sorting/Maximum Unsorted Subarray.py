'''
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        l=sorted(A)
        L = [ i for i in range(A.__len__()) if A[i]!=l[i] ]
        return ([-1] if(A==l) else ([min(L),max(L)]))
