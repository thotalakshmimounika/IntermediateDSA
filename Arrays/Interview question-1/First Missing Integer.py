a=[3, 4, -1, 1]
n=len(a)
for i in range(n):
    val=a[i]
    while(i!=val-1 and a[i]>0):
        temp= a[val-1]
        a[val-1]=val
        a[i]=val
print(n+1)