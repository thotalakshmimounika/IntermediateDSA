a=[0,0,0]
b=0
n=len(a)
d={}
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=a[j]
        if s==b:
            c+=1
print(c)

