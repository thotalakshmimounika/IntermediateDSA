a=[ 5, 9, 10, 4, 7, 8 ]
b=[ 5, 6, 4, 7, 2, 5 ]

n=len(a)
ans=10000
for j in range(1,n-1):
    for i in range(j-1,-1,-1):
        if a[i]<a[j]:
            cost=0
            for k in range(j+1,n):
                if a[k]>a[j]:
                    cost+=b[i]+b[j]+b[k]
                    break
            ans=min(ans,cost)
print(ans)