'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

'''
def is_largest(a,b):
    return 1 if a+b>b+a else -1
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        from functools import cmp_to_key
        A=map(str,A)
        res="".join(sorted(A,key=cmp_to_key(is_largest),reverse=True))
        if int(res)==0:return '0'
        res=list(res)
        for j in range(len(res)):
            if res[j]!='0':break
        return "".join(res[j:])
        
 #ANOTHER WAY
 '''
 class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self,A): 
          
        # extval is a empty list for extended  
        # values and ans for calculating answer 
        extval, ans = [], "" 
          
        # calculating the length of largest number 
        # from given and add 1 for further operation 
        l = len(str(max(A))) + 1
          
        # iterate given values and  
        # calculating extended values 
        for i in A: 
            temp = str(i) * l 
              
            # make tuple of extended value and  
            # equivalant original value then  
            # append to list 
            extval.append((temp[:l:], i)) 
          
        # sort extval in descending order 
        extval.sort(reverse = True) 
          
        # iterate extended values 
        for i in extval: 
              
            # concatinate original value equivalant 
            # to extended value into ans variable 
            ans += str(i[1]) 
              
        return int(ans)
'''
