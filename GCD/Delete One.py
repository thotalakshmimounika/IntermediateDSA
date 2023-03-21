def gcd(l,r):
    if r==0 or l==0:
        return l
    else:
        return gcd(r,l%r)
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=len(a)
        pgcd=[0]*n
        pgcd[0]=a[0]
        for i in range(1,n):
            pgcd[i]=pgcd[i-1]+a[i]
        sgcd=[0]*n
        sgcd[n-1]=a[n-1]
        for i in range(n-2,-1,-1):
            sgcd[i]=sgcd[i+1]+a[i]
        ans=0
        for i in range(1,n-1):
            left=pgcd[i-1]
            right=sgcd[i+1]
            ans = max(gcd(left,right),ans)
        return ans
obj=Solution()
print(obj.solve([12, 15, 18]))