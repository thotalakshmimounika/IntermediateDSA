a='scaler'
b=[[0,2],[2,4]]
# @param A : string
# @param B : list of list of integers
# @return a list of integers
def solve(self, a,b):
    n=len(a)
    ans='aeiou'
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+(a[i-1] in ans)
    k=[]
    for i in range(len(b)):
        l,r=b[i]
        c=p[r+1]-p[l]
        k.append(c)
    return k
