# Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.



# Problem Constraints
# 1 <= A <= 105



# Input Format
# First and only argument is an integer A.



# Output Format
# Return an integer denoting the minimum count.



# Example Input
# Input 1:

#  A = 6
# Input 2:

#  A = 5


# Example Output
# Output 1:

#  3
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
#  Minimum count of numbers, sum of whose squares is 6 is 3. 
# Explanation 2:

#  We can represent 5 using only 2 numbers i.e. 12 + 22 = 5

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, a):
        dp=[-1]*(a+1)
        dp[0],dp[1]=0,1
        for i in range(2,a+1):
            ans=float('inf')
            for j in range(1,int(i**0.5)+1):
                ans=min(ans,dp[i-j**2])
            dp[i]=ans+1
        return dp[a]
#Tc- O(Nsrt(N))
#SC- O(N)