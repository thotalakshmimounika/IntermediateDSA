#Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
a=[1,2,3],[4,5,6],[7,8,9]
n=len(a)
ans=[[0]*n for _ in range(2*n-1)]
print(ans)
r=-1
c=-1
for i in range(n):

    startcol = i
    startrow = 0
    r+=1
    c=0

    while(startcol >= 0 and startrow < n):
        ans[r][c]=a[startrow][startcol]
        startcol -= 1
        startrow += 1
        c+=1
r=n-1
c=0
for i in range(1, n):
        startrow = i
        startcol = n - 1
        r+=1
        c=0
 
        while(startrow < n and startcol >= 0):
            ans[r][c]=a[startrow][startcol]
 
            startcol -= 1
            startrow += 1
            c+=1
 
print(ans)