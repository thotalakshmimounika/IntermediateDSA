a= [   [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]   ]
n=len(a)
m=len(a[0])
for i in range(n):
    for j in range(1,m):
        a[i][j]=a[i][j-1]+a[i][j]
for i in range(m):
    for j in range(1,n):
        a[j][i]=a[j-1][i]+a[j][i]
print(a)
