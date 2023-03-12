A=11
s=0
i=1
for x in range(10):
    m1=max((A%(i*10))-(i-1),0)
    m2=min(m1,i)
    ans=(A//(i*10))
    c=ans*i
    t=c+m2
    s=s+t
    i=i*10
print(s)
