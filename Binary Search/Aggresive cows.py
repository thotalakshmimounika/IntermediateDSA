def CheckcowsfitinMiddist(mid,a,b):
    lastposition=a[0]
    cowscount=1
    for i in range(1,len(a)):
        if a[i]-lastposition>=mid:
            cowscount+=1
            lastposition=a[i]
        if cowscount==b:
            return True
    return False
a = [1, 2, 3, 4, 5]
b = 3
left=1
right=a[-1]-a[0]
ans=0
while(left<=right):
    mid=(left+right)//2
    if CheckcowsfitinMiddist(mid,a,b):
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)
