# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# NOTE:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=len(a)
        for i in range(1,n):
            a[i]=a[i]+a[i-1]
            
        for i in range(n):
            if i==0:
                val = 0
            else:
                val = a[i-1]

            if val == a[n-1] - a[i]:
                return i

        return -1
