'''
Problem Description

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.

'''

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        def pat_form(n):
            n = str(n)
            temp = n[0]
            c = 1
            result = ""
            for number in  n[1:]:
                if(temp == number):
                    c+=1
                    continue
                else:
                    result = result +  str(c)
                    result = result + temp
                    temp = number
                    c=1
                    continue
            result =  result + str(c)
            result =  result + temp
            return (int(result))
        output = 1
        for _ in range(A - 1):
            output = pat_form(output)
        
        return output
