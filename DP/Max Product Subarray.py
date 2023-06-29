# Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

# Return an integer corresponding to the maximum product possible.

# NOTE: Answer will fit in 32-bit integer value.



# Problem Constraints
# 1 <= N <= 5 * 105

# -100 <= A[i] <= 100



# Input Format
# First and only argument is an integer array A.



# Output Format
# Return an integer corresponding to the maximum product possible.



# Example Input
# Input 1:

#  A = [4, 2, -5, 1]
# Input 2:

#  A = [-3, 0, -5, 0]


# Example Output
# Output 1:

#  8
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  We can choose the subarray [4, 2] such that the maximum product is 8.
# Explanation 2:

#  0 will be the maximum product possible.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, a):
        a=list(a)
        n=len(a)
        dp_min=[1]*n
        dp_max=[1]*n
        dp_min[0],dp_max[0]=a[0],a[0]

        for i in range(1,n):
            temp_max = max(a[i], a[i] * dp_min[i - 1], a[i] * dp_max[i - 1])
            temp_min = min(a[i], a[i] * dp_min[i - 1], a[i] * dp_max[i - 1])
            dp_max[i] = temp_max
            dp_min[i] = temp_min

        return max(dp_max)

