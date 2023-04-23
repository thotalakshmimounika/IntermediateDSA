class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        s=set(a)
        m=max(a)
        c=0
        for i in range(1,m+1):
            if i in s:
                continue
            else:
                c+=1
            if c==b:
                return i
        return n+b
            
