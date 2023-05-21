a=["ccbc","aacc","ab","a","da","ccc","aa","dbb","dcd"]
b=["b","a","d","ccdd","abc","caa","bc","ccc","baac","ccb"]
print(a[0])
d1={}
for i in a:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
d2={}
for j in b:
    if j in d2:
        d2[j]+=1
    else:
        d2[j]=1
c=0
for i in a:
    if d1[i]==1:
        if i in d2 and d2[i]==1:
            c+=1
print(c)
            
            
            
            
            
            
            