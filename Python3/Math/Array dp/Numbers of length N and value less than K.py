'''
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

 NOTE: All numbers can only have digits from the given set. 
Examples:

	Input:
	  0 1 5  
	  1  
	  2  
	Output:  
	  2 (0 and 1 are possible)  

	Input:
	  0 1 2 5  
	  2  
	  21  
	Output:
	  5 (10, 11, 12, 15, 20 are possible)
Constraints:

    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
'''
MAX=10
def numToVec(N): 
          
        digit = [] 
        while (N != 0): 
            digit.append(N % 10) 
            N = N // 10
      
         
        if (len(digit) == 0): 
            digit.append(0) 
      
        
        digit = digit[::-1] 
        return digit 
      
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C): 
        d, d2 = 0,0
     
        digit = numToVec(C) 
        d = len(A) 
      
        if (B > len(digit) or d == 0): 
            return 0
      
        
        elif (B < len(digit)): 
            # contain 0 
            if (A[0] == 0 and B != 1): 
                return (d - 1) * pow(d, B - 1) 
            else: 
                return pow(d, B) 
      
        
        else : 
            dp=[0 for i in range(B + 1)] 
            lower=[0 for i in range(MAX + 1)] 
      
            
            for i in range(d): 
                lower[A[i] + 1] = 1
            for i in range(1, MAX+1): 
                lower[i] = lower[i - 1] + lower[i] 
      
            flag = True
            dp[0] = 0
            for i in range(1, B+1): 
                d2 = lower[digit[i - 1]] 
                dp[i] = dp[i - 1] * d 
      
                # For first index we can't use 0 
                if (i == 1 and A[0] == 0 and B != 1): 
                    d2 = d2 - 1
      
                
                if (flag): 
                    dp[i] += d2 
      
                flag = (flag & (lower[digit[i - 1] + 1] == lower[digit[i - 1]] + 1)) 
              
            return dp[B]  
