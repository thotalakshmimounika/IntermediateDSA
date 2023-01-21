a=[1,2,2,3]

n=len(a)
p=a[0]
k=0
d=0
if p<=a[1]:
    for i in range(1,n):
        if a[i]>=p:
            p=a[i]
            k+=1
            if k==n-1:
                Print('True')
else:
    for i in range(1,n):
        if a[i]<=p:
            p=a[i]
            d+=1
            if d==n-1:
                Print('True')
Print('False')