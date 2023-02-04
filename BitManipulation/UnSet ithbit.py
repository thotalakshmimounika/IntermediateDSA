# You are given two integers A and B.
# If B-th bit in A is set, make it unset
# If B-th bit in A is unset, leave it as it is
# Return the updated A value


# Problem Constraints
# 1 <= A <= 109
# 0 <= B <= 30


# Input Format
# First argument A is an integer.
# Second argument B is an integer.


# Output Format
# Return an integer.


# Example Input
# Input 1:
# A = 4
# B = 1
# Input 2:
# A = 5
# B = 2


# Example Output
# Output 1:
# 4
# Output 2:
# 1


# Example Explanation
# For Input 1:
# Given N = 4 which is 100 in binary. The 1-st bit is already unset
# For Input 2:
 
# Given N = 5 which is 101 in binary. We unset the 2-nd bit
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        return (a|(1<<b))^(1<<b)
