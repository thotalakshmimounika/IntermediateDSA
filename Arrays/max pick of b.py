a=[5,-2,3,1,2]
b=3
i=0
n=len(a)
while i<n-1:
    if a[i]>a[i+1]:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
        i=-1
    i+=1
print(a)
s=0
for i in range(b):
    s=s+a[n-1-i]
print(s)


