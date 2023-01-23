#You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.
a=[1,2,3,4],[5,6,7,8],[9,2,3,4]

n=len(a)
m=len(a[0])
res=[]
for j in range(m):
    s=0
    for i in range(n):
        s+=a[i][j]
    res.append(s)
print(res)