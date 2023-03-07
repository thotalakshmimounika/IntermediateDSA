A=[-5,-4,-3],[-1,2,3],[2,2,4]

n=len(A)
m=len(A[0])
for i in range(n):
    for j in range(1,m):
        A[i][j]=A[i][j-1]+A[i][j]
for i in range(m):
    for j in range(1,n):
        A[j][i]=A[j-1][i]+A[j][i]
brr = len(A)-1
brc = len(A[0])-1
maxsum = A[brr][brc]
for tlr in range(brr + 1):
    for tlc in range(brc + 1):
        sum = 0
        if tlr <= 0 and tlc <= 0:
            sum = A[brr][brc]
        elif tlr <= 0 and tlc > 0:
            sum = A[brr][brc] - A[brr][tlc-1]
        elif tlr > 0 and tlc <= 0:
            sum = A[brr][brc] - A[tlr-1][brc]
        else:
            sum = A[brr][brc] - A[brr][tlc-1] - A[tlr-1][brc] + A[tlr-1][tlc-1]
        maxsum = max(maxsum,sum)
print(maxsum)