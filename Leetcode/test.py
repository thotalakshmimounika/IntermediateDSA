class Solution:
    import sys
    def maxp3(self,a):
        n=len(a)
        ma=-sys.maxsize-1
        mb=-sys.maxsize-1
        mc=-sys.maxsize-1
        mina=sys.maxsize
        minb=sys.maxsize
        for i in range(n):
            if a[i]>ma:
                mc=mb
                mb=ma
                ma=a[i]
            elif a[i]>mb:
                mc=mb
                mb=a[i]
            elif a[i]>mc:
                mc=a[i]
            if a[i]<mina:
                minb=mina
                mina=a[i]
        return max(mina*minb*mina,ma*mb*mc)
	        
	        
