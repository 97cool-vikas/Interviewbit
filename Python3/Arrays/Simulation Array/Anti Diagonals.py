'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]
'''
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        row_len = len(A)
        col_len = len(A[0])
    
        B = []
        start_row = 0
        start_col = 0
        while True:
            L = []
    
            j = 0
            curr_row = start_row
            for j in range(start_col, col_len):
                L.append(A[j][curr_row])
                if curr_row == 0:
                    break
                curr_row -= 1
            if L:
                B.append(L)
        
            if start_row < row_len - 1:
                start_row += 1
            else:
                start_col += 1
    
            if start_col > (col_len - 1):
                break
            
        return B
