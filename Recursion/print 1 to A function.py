# You are given an integer A, print 1 to A using using recursion.



# Problem Constraints
# 1 <= A <= 104



# Input Format
# First argument A is an integer.



# Output Format
# Print A space-separated integers 1 to A.
# Note: There should be exactly one space after each integer. After printing all the integers, print a new line



# Example Input
# Input 1:

# A = 10
# Input 2:

# A = 5


# Example Output
# Output 1:

# 1 2 3 4 5 6 7 8 9 10 
# Output 2:

# 1 2 3 4 5 


# Example Explanation
# Explanation 1:

# Print 1 to 10 space separated integers.

def printNum(a):
    if a==1:
        print(1,end=' ')
    else:
        printNum(a-1)
        print(a, end=' ')
class Solution:
    # @param A : integer
    def solve(self, a):
        printNum(a)
        print()
