'''
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

1.Integers in each row are sorted from left to right.
2.The first integer of each row is greater than or equal to the last integer of the previous row.

Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A = 
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
'''
def binarySearch(Arr,target) :
    start=0
    end=len(Arr)-1

    while start <= end :
        mid = (start + end) // 2
        if Arr[mid] == target :
            return mid
        
        elif Arr[mid] < target :
            start = mid + 1
        
        else :
            end = mid - 1;
    
    return -1
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        start=0
        end=len(A)-1
        while start<end:
            mid=(start+end)//2
            if A[mid][0]<=B:
                if B<=A[mid][-1]:
                    start=mid
                    break
                start=mid+1
            else:
                end=mid-1
        
        return 1 if binarySearch(A[start],B)!=-1 else 0
