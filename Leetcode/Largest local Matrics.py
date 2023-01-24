a= [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]   

n=len(a)
c=[[0]*(n-2) for _ in range(n-2)]
for i in range(1,n-1):
    for j in range(1,n-1):
        print((a[i-1][j-1], a[i-1][j], a[i-1][j+1],a[i][j-1], a[i][j], a[i][j+1],a[i+1][j-1], a[i+1][j], a[i+1][j+1]))
        c[i-1][j-1] = max(a[i-1][j-1], a[i-1][j], a[i-1][j+1],
                            a[i][j-1], a[i][j], a[i][j+1],
                            a[i+1][j-1], a[i+1][j], a[i+1][j+1])
print(c)
