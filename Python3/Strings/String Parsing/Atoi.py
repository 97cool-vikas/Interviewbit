'''
Please Note:
There are certain questions where the interviewer would intentionally frame the question vague.
The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.

Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

 Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        n = len(A)
        
        for i in range(n):
            if A[0] == ' ':
                A = A[1:]
            else:
                break
        
        num = 0
        pos = True
        for i in range(len(A)):
            if i == 0 and A[i] == '+' :
                pos = True
            elif i == 0 and A[i] == '-':
                pos = False
            elif not ('0' <= A[i] <= '9'):
                return num if pos == True else (-1)*num
            else:
                num = (num) * 10 + int(A[i])
                if num > 2147483647 and pos == True:
                    return 2147483647
                elif num > 2147483647 and pos == False:
                    return -2147483648
                    
        return num if pos == True else (-1) * num       

