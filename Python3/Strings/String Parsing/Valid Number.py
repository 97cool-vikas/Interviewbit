'''
Please Note:
Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.

Please think of all the corner cases and clarifications yourself.

Validate if a given string is numeric.

Examples:

1."0" => true
2." 0.1 " => true
3."abc" => false
4."1 a" => false
5."2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Clarify the question using “See Expected Output”

1.Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
2.Is 0.1e10 valid?
Yes
3.-01.1e-10?
Yes
4.Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
5. 3. (. not followed by a digit)?
No
6.Can exponent have decimal numbers? 3e0.1?
Not for this problem.
7.Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
8.How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
9.How about integers preceded by 00 or 0? like 008?
Yes for this problem
'''
class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        while len(A)>0 and A[0]==' ':
            A = A[1:]
        A=A[::-1]
        while len(A)>0 and A[0]==' ':
            A = A[1:]
        A=A[::-1]
        if len(A)==0:
            return 0
        for c in A:
            if c not in [str(i) for i in range(10)] + ['.', 'e', '-', '+']:
                return 0
        if 'e' in A:
            A = A.split('e')
            if len(A)!=2:
                return 0
            return int(self.isnum(A[0], 0) and self.isnum(A[1], 1))
        return int(self.isnum(A, 0))
        
    def isnum(self, A, i):
        #print(A,i)
        if A=='':
            return False
        if i == 1 or (i == 0 and '.' not in A):
            if A[0] in ['+', '-']:
                A = A[1:]
            if A == '':
                return False
            for c in A:
                if c not in [str(i) for i in range(10)]:
                    return False
            return True
        A = A.split('.')
        return (self.isnum(A[0], 1) or A[0]=='') and self.isnum(A[1], 1)


