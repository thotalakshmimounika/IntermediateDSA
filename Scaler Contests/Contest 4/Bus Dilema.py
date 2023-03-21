class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        p=[0]*n
        p[0]=a[0]
        for i in range(1,n):
            p[i]=p[i-1]+a[i]
            
        maxele=max(p)
        minele=min(p)
        if maxele>b or minele<-b:
            return 0
        low,high=b,0
        if minele>0:
            low=0
        else:
            low=-(minele)
        if maxele>0:
            high=b-maxele
        else:
            high=b
        return high-low+1
            