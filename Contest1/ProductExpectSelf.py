a=[1,2,3,4]
n=len(a)
p=[1]*n
p[0]=a[0]
s=[1]*n
s[n-1]=a[n-1]
b=[]
m=10**9+7
for i in range(1,n):
    p[i]=(p[i-1]*a[i])%m
for i in range(n-2,-1,-1):
    s[i]=(s[i+1]*a[i])%m

for i in range(n):
    if i==0:
        b.append(s[i+1])
    elif i==n-1:
        b.append(p[i-1])
    else:
        b.append((p[i-1]*s[i+1])%m)
print(b)
    
	        
	        
