'''
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, I):
        res = []
        I.sort(key=lambda i: i.start)
        for i in I:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res
      
#Another Way
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import functools
from collections import deque
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    
    def cmp(self,x,y):
        s1=x.start 
        s2=y.start
        e1=x.end
        e2=y.end
        if(s1>s2):
            return 1
        elif(s1==s2):
            if(e1>e2):
                return 1
            else:
                return -1
        else:
            return -1
    def merge(self, intervals):
        intervals=sorted(intervals,key=functools.cmp_to_key(self.cmp))
        
        stack=deque()
        stack.append(intervals[0])
        for idx in range(1,len(intervals)):
            i=intervals[idx]
            top_start=stack[-1].start
            top_end=stack[-1].end
            if(top_end<i.start): #does not overlap
                stack.append(i)
            elif(top_end<i.end): #overlaps
                stack.pop()
                new_I=Interval(top_start,i.end)
                stack.append(new_I)
            
            
        ans=list(stack)
        return ans
'''
