'''
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
'''
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        B = abs(A)
        a = list(str(B))
        a.reverse()
        c = ""
        c = int(c.join(a))
        if c > 2 ** 31:
            return 0
        else:
            if A >= 0:
                return c
            else:
                return -c
