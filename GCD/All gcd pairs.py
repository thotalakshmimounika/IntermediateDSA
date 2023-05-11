def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a= [2, 2, 2, 2, 8, 2, 2, 2, 10]
a.sort(reverse=True)
d={}
ans=[]
for i in a:
    if i in d and d[i]>0:
        d[i]-=1
    else:
        d[i]=1
        for j in ans:
            val=gcd(i,j)
            if val in d:
                d[val]+=2
            else:
                d[val]=2
        ans.append(i)
print(ans)
