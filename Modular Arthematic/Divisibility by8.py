a='56123'
n=len(a)
ans=0
for i in range(n-1,n-4,-1):
    ans+=a[i]
if ans%8==0:
    print(1)
else:
    print(0)
