a=7
n=a
print(n,n*n)
c=[[0]*n for _ in range(n)]
tr=0
br=n-1
rc=n-1
lc=0
x=1
while(x<=n*n):
    for i in range(lc,rc+1):
        c[tr][i]=x
        x+=1
    tr+=1
    for i in range(tr,br+1):
        c[i][rc]=x
        x+=1
    rc-=1
    for i in range(rc,lc-1,-1):
        c[br][i]=x
        x+=1
    br-=1
    for i in range(br,tr-1,-1):
        c[i][lc]=x
        x+=1
    lc+=1

print(c)