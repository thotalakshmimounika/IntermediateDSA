A=2
count=31
ans=0
while A>0:
    if (A&1)==1:
        ans+=(1<<count)
    A = A>>1
    count-=1
print(ans)
