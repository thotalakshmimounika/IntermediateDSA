a= "aa"
b= 3
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
c=[]
for i in d:
    c.append(d[i])
c.sort()

n=len(d)
if n>1:
    for i in c:
        if i<=b:
            b-=i
            n-=1
print(n)
