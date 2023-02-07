a= [2,4,1]
n=len(a)
a.sort()
d=a[1]-a[0]
c=1
for i in range(1,n):
    if a[i]-a[i-1]==d:
        c+=1
if n==c:
    print(1)
else: print(0)