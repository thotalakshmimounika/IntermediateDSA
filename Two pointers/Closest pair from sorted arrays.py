a= [5,10,20]
b = [1,2,30]
c = 13

n=len(a)
m=len(b)
i=0
j=m-1
ans=abs(a[i]+b[j]-c)
res=[a[i],b[j]]
while(i<n and j>=0):
    l=abs(a[i]+b[j]-c)
    if l<=ans:
        if l<ans:
            res[0]=a[i]
            res[1]=b[j]
        elif l==ans and a[i]<=res[0]:
            res[0]=a[i]
            res[1]=b[j]
        ans=min(ans,l)
    if a[i]+b[j]<c:
        i+=1
    else:
        j-=1
print(res)




        
