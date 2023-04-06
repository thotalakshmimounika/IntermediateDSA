a= [1,1,2,2,3,3,4,4,5,6,6,7,7,8,8]
n=len(a)
if n==1:
    print(a[0])
if a[0]!=a[1]:
    print(a[0])
if a[n-1]!=a[n-2]:
    print(a[n-1])
left=2
right=n-3
while(left<=right):
    mid=(left+right)//2
    if a[mid-1]!=a[mid] and a[mid]!=a[mid+1]:
        print(a[mid])
    fo=mid
    if a[mid]==a[mid-1]:
        fo=a[mid-1]
    if fo%2==0:
        left=mid+1
    else:
        right=mid-1
        

