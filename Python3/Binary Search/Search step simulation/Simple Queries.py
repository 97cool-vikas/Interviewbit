'''
Problem Description

You are given an array A having N integers.

You have to perform the following steps in a given order.

1) generate all subarrays of A.

2) take the maximum element from each subarray of A and insert it into a new array G.

3) replace every element of G with the product of their divisors mod 1e9 + 7.

4) sort G in descending order

You now need to perform Q queries

In each query, you are given an integer K, where you have to find the Kth element in G.

NOTE : Your solution will run on multiple test cases so do clear global variables after using them.



Problem Constraints
1 <= N <= 1e5

1 <= A[i] <= 1e5

1 <= Q <= 1e5

1 <= k <= (N * (N + 1))/2



Input Format
The first argument given is an Array A, having N integers.

The second argument given is an Array B, where B[i] is the ith query.



Output Format
Return an Array X, where X[i] will have the answer for the ith query.



Example Input
Input 1:

 A = [1, 2, 4]
B = [1, 2, 3, 4, 5, 6]
Input 2:

 A = [1, 3]
B = [1]


Example Output
Output 1:

 [8, 8, 8, 2, 2, 1]
Output 2:

 [3]


Example Explanation
Explanation 1:

 subarrays of A    maximum element
1. [1] 1
2. [1, 2] 2
3. [1, 2, 4] 4
4. [2] 2
5. [2, 4] 4
6. [4] 4
original G = [1, 2, 4, 2, 4, 4]

after changing every element of G with product of their divisors G = [1, 2, 8, 2, 8, 8]

after sorting G in descending order G = [8, 8, 8, 2, 2, 1]

Explanation 2:

 Just perform given query.
'''
from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        p = [1] * (max(A) + 1)
        for i in range(1, len(p)):
            for j in range(i, len(p), i):
                p[j] = (p[j] * i) % 1000000007
        stack = []
        l = [-1] * len(A)
        r = [len(A)] * len(A)
        for idx, val in enumerate(A):
            while len(stack):
                stackIdex, stackValue = stack[-1]
                if stackValue < val:
                    r[stackIdex] = idx
                    stack.pop()
                else:
                    l[idx] = stackIdex
                    break
            stack.append((idx, val))
        g = [(p[A[i]], (i - lr[0]) * (lr[1] - i)) for i, lr in enumerate(zip(l, r))]
        length = 0
        G = []
        for p, count in sorted(g, reverse=True):
            length += count
            G += [(length, p)]
        Q = []
        return [G[bisect_left(G, (q,0))][1] for q in B]
        
        
