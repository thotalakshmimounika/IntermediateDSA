a=[-5,-4,-3],[-1,2,3],[2,2,4]
n=len(a)
m=len(a[0])
for i in range(n):
    for j in range(1,m):
        a[i][j]=a[i][j-1]+a[i][j]
for i in range(m):
    for j in range(1,n):
        a[j][i]=a[j-1][i]+a[j][i]
print(a)
ans = float('-inf')
bru=n-1
brd=m-1
ms=a[bru][brd]
for tlu in range(n):
    for tld in range(m):
        s=0
        if tlu<=0 and tld<=0:
            s=a[bru][brd]
        elif tlu<=0 and tld>0:
            s=a[bru][brd]-a[bru][tld-1]
        elif tlu>0 and tld<=0:
            s=a[bru][brd]-a[tlu][brd]
        else:
            s=a[bru][brd]-a[bru][tld-1]-a[tlu][brd]+a[tlu-1][bru-1]
        ms=max(ms,s)
print(ms)

                
