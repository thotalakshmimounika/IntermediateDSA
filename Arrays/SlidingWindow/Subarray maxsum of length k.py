# Given an array A of length N. Also given are integers B and C.

# Return 1 if there exists a subarray with length B having sum C and 0 otherwise



# Problem Constraints
# 1 <= N <= 105

# 1 <= A[i] <= 104

# 1 <= B <= N

# 1 <= C <= 109



# Input Format
# First argument A is an array of integers.

# The remaining arguments B and C are integers



# Output Format
# Return 1 if such a subarray exist and 0 otherwise


# Example Input
# Input 1:
# A = [4, 3, 2, 6]
# B = 2
# C = 5
# Input 2:

# A = [4, 2, 2]
# B = 2
# C = 8


# Example Output
# Output 1:
# 1
# Output 2:

# 0


# Example Explanation
# Explanation 1:
# The subarray [3, 2] is of length 2 and sum 5.
# Explanation 2:
# There are no such subarray.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, a, b, c):
        n=len(a)
        s=0
        for i in range(0,b):
            s+=a[i]
        if s==c:
            return 1
        start=1
        end=b
        while(end<n):
            s+=a[end]-a[start-1]
            if s==c:
                return 1
                break
            start+=1
            end+=1
        return 0

 # Time Complexity -O(N)
 # Space Complexity -O(1)

