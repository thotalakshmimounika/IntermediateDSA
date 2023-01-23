a= [ 1, 2, 3, 4, 5 ]
n=len(a)
p=[1]*n
lp=1
for i in range(n):
    p[i]=lp
    lp*=a[i]
rp=1
for i in range(n-1,-1,-1):
    p[i]=rp
    rp*=a[i]
print(p) 