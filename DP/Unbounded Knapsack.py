# Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.

# This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.



# Problem Constraints
# 1 <= A <= 1000

# 1 <= |B| <= 1000

# 1 <= B[i] <= 1000

# 1 <= C[i] <= 1000



# Input Format
# First argument is the Weight of knapsack A

# Second argument is the vector of values B

# Third argument is the vector of weights C



# Output Format
# Return the maximum value that fills the knapsack completely



# Example Input
# Input 1:

# A = 10
# B = [5]
# C = [10]
# Input 2:

# A = 10
# B = [6, 7]
# C = [5, 5]


# Example Output
# Output 1:

#  5
# Output 2:

# 14


# Example Explanation
# Explanation 1:

# Only valid possibility is to take the given item.
# Explanation 2:

# Take the second item twice.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, c,a,b):
        n=len(a)
        d=[[0]*(c+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,c+1):
                if j>=b[i-1]:
                    d[i][j] =max(d[i-1][j],a[i-1]+d[i][j-b[i-1]])
                else:
                    d[i][j]=d[i-1][j]
        return d[n][c]

#TC- O(N*M)
#Sc- O(N*M)
