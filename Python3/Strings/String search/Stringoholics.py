'''
Problem Description

You are given an array A consisting of strings made up of the letters 'a' and 'b' only.
Each string goes through a number of operations, where:

1.  At time 1, you circularly rotate each string by 1 letter.
2.  At time 2, you circularly rotate the new rotated strings by 2 letters.
3.  At time 3, you circularly rotate the new rotated strings by 3 letters.
4.  At time i, you circularly rotate the new rotated strings by i % length(string) letters.


Eg: String is "abaa"




1. At time 1, string is "baaa", as 1 letter is circularly rotated to the back

2. At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back

3. At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back

4. At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back

5. At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back

After some units of time, a string becomes equal to its original self.
Once a string becomes equal to itself, it's letters start to rotate from the first letter again (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be its original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 109+7.

Note: Your solution will run on multiple test cases so do clear global variables after using them.



Input Format
A: Array of strings.



Output Format
Minimum time, where maximum number of strings are equal to their original self.



Example Input
Input 1:

  A: [a, ababa, aba]
Input 2:

  A : [a, aa]


Example Output
Output 1:

  4
Output 2:

  1


Example Explanation
Explanation 1:

  String 'a' is it's original self at time 1, 2, 3 and 4.
String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
String 'aba' is it's original self at time 2 and 4. (aba => baa => aba)
Hence, 3 strings are their original self at time 4.
Explanation 2:

  Both strings are their original self at time 1.
'''


class Solution:
    def gcd(self, a, b):
        if b > a:
            a, b = b, a
        if b == 0: return a
        return self.gcd(b, a%b)
 
    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
 
    def computeLPSArray(self, pat):
        i=(pat+pat).find(pat,1,-1)
        return len(pat) if i == -1 else len(pat[:i])
 
    def solve(self, A):
        n = len(A)
        ans = 1
        for s in A:
            res = self.computeLPSArray(s)
            for i in range(1, 2*res+1):
                if ((i*(i+1))//2)%res == 0:
                    ans = self.lcm(ans, i)
                    break
        return ans % 1000000007
