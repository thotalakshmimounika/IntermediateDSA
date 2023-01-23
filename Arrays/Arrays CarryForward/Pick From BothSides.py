# You are given an integer array A of size N.

# You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4, and array A contains 10 elements, then

# You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.
class Solution:
    def solve(self, A, B):
        s = sum(A[:B])
        if B == len(A)-1:
            return s
           
             
        m  = s
        for i in range(B):
            s -= A[B-1-i]
            s += A[len(A)-1-i]
            m = max(m,s)
       
        return m
            