# Given the total number of person A and a number B which indicates that B-1 persons are skipped and the Bth person is killed in a circle. Find the last person standing in the circle.


# Problem Constraints
# 1 <= A <= 104
# 2 <= B <= A



# Input Format
# First argument A is an integer.
# Second argument B is an integer.


# Output Format
# Return an integer.


# Example Input
# Input 1:
# A = 4
# B = 2
# Input 2:
# A = 5
# B = 3


# Example Output
# Output 1:
# 1
# Output 2:
# 4


# Example Explanation
# For Input 1:
# Firstly, the person at position 2 is killed, then the person at position 4 is killed,
# then the person at position 3 is killed. So the person at position 1 survives. 
# For Input 2:
# Firstly, the person at position 3, then the person at position 1 is killed, 
# then the person at position 5 is killed. Finally, the person at position 2 is killed. 
# So the person at position 4 survives. 

import sys
sys.setrecursionlimit(10**6)
def jos(n,k):
    if n==1:
        return 0
    else:
        return (jos(n-1,k)+k)%n
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        return jos(a,b)+1