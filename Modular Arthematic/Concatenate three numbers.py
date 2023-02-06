# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.

# Return the minimum result obtained.



# Problem Constraints
# 10 <= A, B, C <= 99



# Input Format
# The first argument of input contains an integer, A.

# The second argument of input contains an integer, B.

# The third argument of input contains an integer, C.



# Output Format
# Return an integer representing the answer.



# Example Input
# Input 1:

#  A = 10
#  B = 20
#  C = 30
# Input 2:

#  A = 55
#  B = 43
#  C = 47 


# Example Output
# Output 1:

#  102030 
# Output 2:

#  434755 


# Example Explanation
# Explanation 1:

#  10 + 20 + 30 = 102030 
# Explanation 2:

#  43 + 47 + 55 = 434755 
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self,a,b,c):
        ans=0
        x=min(a,b)
        x2=min(x,c)
        ans+=x2*10000
        y=max(a,b)
        y1=max(y,c)
        z=max(x,c)
        z2=min(y,z)
        ans+=z2*100
        ans+=y1
        return ans