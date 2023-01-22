a = [[1, 2],[1,2],[1,2]]
n=len(a)
m=len(a[0])
print(a,n,m)
c=[[0]*n for i in range(m)]
for i in range(n):
    for j in range(m):
        c[j][i]=a[i][j]

print(c)