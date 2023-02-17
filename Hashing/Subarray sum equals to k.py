a=[0,0,0]
b=0
n=len(a)
s=0
d={}
c=0
for i in range(n):
    s+=a[i]

    if s==b:
        c+=1
    if s-b in d:
        c+=d[s-b]
    d[s]=i
print(c)
