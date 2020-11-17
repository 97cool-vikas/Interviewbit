'''
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

1.X divides A i.e. A % X = 0
2.X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        def cpFact(self, A, B):
            while True:
                temp=Solution.gcd(A,B)
                if temp==1:break
                A = A // temp
            return A
        def gcd(a,b):
            if a==0: return b
            else: return Solution.gcd(b%a,a)
