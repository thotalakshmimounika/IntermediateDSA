# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.

# Note: Return the two numbers in ascending order.


# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109



# Input Format
# The first argument is an array of integers of size N.



# Output Format
# Return an array of two integers that appear only once.



# Example Input
# Input 1:
# A = [1, 2, 3, 1, 2, 4]
# Input 2:

# A = [1, 2]


# Example Output
# Output 1:
# [3, 4]
# Output 2:

# [1, 2]


# Example Explanation
# Explanation 1:
# 3 and 4 appear only once.
# Explanation 2:

# 1 and 2 appear only once.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, a):
        n=len(a)
        ans=0
        for i in range(n):
            ans=ans^a[i]
        for i in range(31):
            if ans&(1<<i):
                c=i
                break
        ta1=0
        ta2=0
        for i in range(n):
            if a[i]&(1<<c):
                ta1=ta1^a[i]
            else:
                ta2=ta2^a[i]
        if ta1<ta2:
            return [ta1,ta2]
        return [ta2,ta1]

# Time complexity - O(N+32+N)~ O(N)
#Space Complexity - O(N)