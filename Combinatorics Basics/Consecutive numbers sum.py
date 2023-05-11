# Given a positive integer A.

# Return the number of ways it can be written as a sum of consecutive positive integers.



# Problem Constraints
# 1 <= A <= 109



# Input Format
# The first and the only argument of input contains an integer, A.



# Output Format
# Return an integer, representing the answer as described in the problem statement.



# Example Input
# Input 1:

#  A = 5
# Input 2:

#  A = 15


# Example Output
# Output 1:

#  2
# Output 2:

#  4


# Example Explanation
# Explanation 1:

#  The 2 ways are:
#  => [5]
#  => [2, 3]
# Explanation 2:

#  The 4 ways are:
#  => [15]
#  => [7, 8]
#  => [4, 5, 6] 
#  => [1, 2, 3, 4, 5]

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, a):
        res=0
        s=0
        for i in range(1,a+1):
            s+=(i-1)
            if s>=a:
                break
            if (a-s)%i==0:
                res+=1
        return res


