# a=[16,3,3,6,7,8,17,13,7]
# b=[0,1,0,1,0,0,1,1,0]
a=[1,4,2,8]
b=[0,0,0,1]
c=2
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, a,b,c):
        n=len(a)
        pf=[0]*n
        pf[0]=a[0]
        for i in range(1,n):
            pf[i]=pf[i-1]+a[i]
        pf1=[0]*n 
        if b[0]==1:
            pf1[0]=a[0]
        for i in range(1,n):
            if b[i]==1:
                pf1[i]=pf1[i-1]+a[i]
            else:
                pf1[i]=pf1[i-1]
        
        s,e=0,c-1
        ans=0
        while(e<n):
            ta=0
            if s==0:
                ta+=pf[e]
            else:
                ta+=pf[e]-pf[s-1]
            if s==0:
                ta+=pf1[n-1]-pf1[e]
            else:
                ta+=pf1[s-1]
                ta+=pf1[n-1]-pf1[e]
            ans=max(ans,ta)
            s+=1
            e+=1
        return ans
                
        

                
        
