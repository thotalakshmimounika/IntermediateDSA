a=123
l=[]
while(a>0):
    l.append(a%10)
    a=a//10
d=set()
for i in range(len(l)):
    p=1
    for j in range(i,len(l)):
        p*=l[j]
        if p in d:
            print(0)
        d.add(p)




