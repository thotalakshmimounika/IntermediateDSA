a= [[1,1,0],[1,0,1],[0,0,0]]
n=len(a)
for i in range(n):
    x=0
    y=n-1
    while(x<=y):
        temp=a[i][x]
        a[i][x]=a[i][y]
        a[i][y]=temp
        x+=1
        y-=1
print(a)
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            a[i][j]=0
        else:
            a[i][j]=1
print(a)