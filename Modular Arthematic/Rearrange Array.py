# Given an array A of size N. Rearrange the given array so that A[i] becomes A[A[i]] with O(1) extra space.

# Constraints:

# 1 <= N <= 5×104

# 0 <= A[i] <= N - 1

# The elements of A are distinct

# Input Format

# The argument A is an array of integers

# Example 1:

# Input : [1, 0]
# Return : [0, 1]
# Example 2:

# Input : [0, 2, 1, 3]
# Return : [0, 1, 2, 3]

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        N = len(A)
        for i in range(N):
            A[i]+= (A[A[i]]%N)*N
        for i in range(N):
            A[i]//=N
        return A