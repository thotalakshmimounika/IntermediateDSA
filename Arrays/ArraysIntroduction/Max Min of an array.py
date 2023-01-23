class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        h=a[0]
        l=a[0]
        for i in range(1,len(a)):
            if h<a[i]:
                h=a[i]
            if l>a[i]:
                l=a[i]
        return l+h