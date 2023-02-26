a=[2,4,3,6,2]
b=3
d={}
s=0
c=0
for i in range(len(a)):
    s+=a[i]
    s=s%b
    if s in d:
        d[s]+=1
    else:
        d[s]=1
for i in d:
    l=d[i]
    if i==0:
        c=c+(l*(l-1))//2+l
    else:
        c=c+(l*(l-1))//2
print(c)