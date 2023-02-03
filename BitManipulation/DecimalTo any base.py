a= 4
b= 3
i=0
ans=0
while(a!=0):
    ans+=a%b*10**i
    a=a//b
    i+=1
print(ans)