a=[0,0,0,0,0,1,0,0]
k=0
n=len(a)
p=[0]*(n+2)
for i in range(1,len(p)-1):
    p[i]=a[i-1]
for i in range(1,len(p)-1):
    if p[i]==0:
        if p[i-1]==0 and p[i+1]==0:
            p[i]=1
            k-=1
    if k==0:
        print("True")