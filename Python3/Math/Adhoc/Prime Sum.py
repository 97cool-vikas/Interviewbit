'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        sieve = [True for i in range(1,A+1)]
        k = 2
        while (k*k < A+1):
            if sieve[k] == True:
                for i in range(k*k,A,k):
                    sieve[i] = False
            k+=1
        
        for i in range(2,A):
            if sieve[A-i] and sieve[i]:
                return [i,A-i]
