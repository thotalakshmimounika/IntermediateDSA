a= (1, 2,5,3,6)
a=list(a)
n=len(a)
if a==[] or n==1:
    print(0)
b=a[0]
p=0
for i in range(1,n):
    if a[i]>b:
        p=max(p,a[i]-b)
    if a[i]<b:
        b=a[i]
print(p)