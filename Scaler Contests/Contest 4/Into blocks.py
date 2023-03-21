a=[1,2,3,1,2,3,3,1,5,4,4,5,4] --- [1,1,1,1,1,1,1,1,4,4,4,4,4]
print(len(a))
d={}
n=len(a)
for i in range(n):
    if a[i] in d:
        d[a[i]][1]=i
    else:
        d[a[i]]=[i,i]
print(d)
m=len(d)
pairarray=[]
for key in d:
    v=d[key]
    pairarray.append(v)
print(pairarray,len(pairarray),m)
pairarray.sort(key=lambda x:x[0])
l=pairarray[0][0]
r=pairarray[0][1]
ans=[]
for i in range(m):
    if r>=pairarray[i][0]:
        r=max(pairarray[i][1],r)
    else:
        ans.append([l,r])
        l=pairarray[i][0]
        r=pairarray[i][1]
ans.append([l,r])
print(ans)
d2={}
for i in a:
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1
print(d2)
final=0
for i in range(len(ans)):
    l,r=ans[i]
    print(l,r)
    maxf=0
    for i in range(l,r+1):
        f=d2[a[i]]
        maxf=max(maxf,f)
    final+=(r-l+1)-maxf
print(final)

