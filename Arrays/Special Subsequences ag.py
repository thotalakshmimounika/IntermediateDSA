a = "ABCGAG"
n=len(a)
print(n)
acount=0
ans=0
for i in range(n):
    if a[i]=='A':
        acount+=1
    if a[i]=='G':
        ans=ans+acount
print(ans)