class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        ans=0
        for i in a:
            ans+=i
        if ans%3==0:
            return 1
        return 0