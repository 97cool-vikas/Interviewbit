'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
'''

class Solution:
	# @param A : string
	# @return a list of strings
	
	def is_valid(self, s):
        IP = s.split('.')
        for i in IP:
            if len(i)>0 and len(str(int(i)))!=len(i):
                return False
            elif int(i)<0 or int(i)>255:
                return False
        return True

    def restoreIpAddresses(self, A):
        if len(A)>12 or len(A)<4:
            return []
        res = []
        for i in range(1, len(A)-2):
            for j in range(i+1, len(A)-1):
                for k in range(j+1, len(A)):
                    s = A[:k]+"."+A[k:]
                    s = s[:j]+"."+s[j:]
                    s = s[:i]+"."+s[i:]
                    if self.is_valid(s):
                        res.append(s)
        return res


