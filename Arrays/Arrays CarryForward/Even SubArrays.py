# You are given an integer array A.

# Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

# Return "YES" if it is possible; otherwise, return "NO" (without quotes).
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, a):
        n=len(a)
        if n<2:
            return "NO"
        elif n%2==0:
            if a[0]%2==0 and a[n-1]%2==0:
                return "YES"

        return "NO"