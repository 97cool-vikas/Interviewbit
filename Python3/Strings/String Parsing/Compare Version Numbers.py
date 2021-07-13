'''
Problem Description

Compare two version numbers version1 and version2.

"1.If version1 > version2 return 1,
2.If version1 < version2 return -1,
3.otherwise return 0."

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = A.split(".")
        b = B.split(".")
        l_range = len(a) if len(a) > len(b) else len(b)
        i = 0
        while i < l_range:
            try:
                if int(a[i]) > int(b[i]):
                    return 1
                elif int(b[i]) > int(a[i]):
                    return -1
            except: 
                if len(b) > len(a):
                    a.append(0)
                else: 
                    b.append(0)
                continue
            i += 1
                
        return 0
        
