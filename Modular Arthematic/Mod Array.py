a=[ 1, 8, 4, 5, 0, 8, 0 ]
b=9
n=len(a)
p=1
ans=0
for i in range(n-1,-1,-1):
    ans=(ans%b+(a[i]%b * (p)%b))%b
    p= (p%b *10%b)%b
print(ans)

