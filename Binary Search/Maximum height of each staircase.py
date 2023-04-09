# Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max-height using these blocks.

# The first stair would require only one block, and the second stair would require two blocks, and so on.

# Find and return the maximum height of the staircase.



# Problem Constraints
# 0 <= A <= 109


# Input Format
# The only argument given is integer A.



# Output Format
# Return the maximum height of the staircase using these blocks.



# Example Input
# Input 1:

#  A = 10
# Input 2:

#  A = 20


# Example Output
# Output 1:

#  4
# Output 2:

#  5


# Example Explanation
# Explanation 1:

#  The stairs formed will have height 1, 2, 3, 4.
# Explanation 2:

#  The stairs formed will have height 1, 2, 3, 4, 5.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, a):
        if a==0 or a==1:
            return a
        height=0
        for i in range(1,a):
            x=(i*(i+1))//2
            if x>a:
                break
            height+=1
        return height
#Time complexity - O(logn)
#space complexity - O(1)