a = [4, 3, 5, 3, 5, 3, 2, 1]
b= 47
n=len(a)
p=1
ans=0
for i in range(n-1,-1,-1):
    ans+=(a[i]%b * (p)%b)%b
    p= (p%b * 10%b)%b
print(ans)

