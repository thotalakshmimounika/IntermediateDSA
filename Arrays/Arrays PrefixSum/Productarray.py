a = [1, 2, 3, 4, 5]
n=len(a)
ans=[0]*n
p=[1]*n
p[0]=a[0]
s=[1]*n
s[n-1]=a[n-1]

for i in range(1,n):
    p[i]=p[i-1]*a[i]
for i in range(n-2,-1,-1):
    s[i]=s[i+1]*a[i]
print(p,s)
for i in range(n):
    if i==0:
        ans[i]=s[i+1]
    elif i==n-1:
        ans[i]=p[i-1]
    else:
        ans[i]=(p[i-1]*s[i+1])
print(ans)

