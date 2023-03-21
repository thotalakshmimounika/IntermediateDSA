class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        MaxAnd=max(a)
        MaxOr=0
        for i in range(len(a)):
            MaxOr=MaxOr|a[i]
        return MaxAnd+MaxOr