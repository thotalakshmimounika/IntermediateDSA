a=[ 1, 3, 2, 4, 5 ]

n=len(a)
p1=0
p2=n-1

for i in range(1,n):
    if a[i]<a[i-1]:
        p1=i-1
        break
for i in range(n-1,0,-1):
    if a[i]<a[i-1]:
        p2=i
        break
if p1==0 and p2==n-1:
    print(-1)
minele=a[p1]
maxele=a[p1]
for i in range(p1+1,p2+1):
    minele=min(a[i],minele)
    maxele=max(a[i],maxele)
x1,x2=0,0
for i in range(n):
    if a[i]>minele:
        x1=i
        break
for i in range(n-1,-1,-1):
    if a[i]<maxele:
        x2=i
        break
print([x1,x2])





