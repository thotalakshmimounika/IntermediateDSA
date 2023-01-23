a=[ 8, 6, 7, 10, 3, 10, 10, 3 ]
b=[[0, 4],[4, 7],[2, 7],[6, 7],[6, 7],[0, 1],[2, 6],[4, 6],[0, 1],[1, 2]]
n=len(a)
p=[0]*(n+1)
for i in range(1,len(a)+1):
    if a[i-1]%2==0:
        p[i]=1+p[i-1]
    else:
        p[i]=p[i]+p[i-1]
print(p)
c=[]
for i in range(len(b)):
    x,y=b[i]
    c.append(p[y+1]-p[x])
print(c)
