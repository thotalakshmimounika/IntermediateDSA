a= "cat"
b= "bat"
d1={}
d2={}
for i in range(len(a)):
    if a[i] in d1:
        d1[a[i]]+=1
    else:
        d1[a[i]]=1
for i in range(len(b)):
    if b[i] in d2:
        d2[b[i]]+=1
    else:
        d2[b[i]]=1  

for i in range(len(a)):
    if a[i] in d1:
        if a[i] in d2 and d1[a[i]]==d2[a[i]]:
            continue
        else:
            print(0)
print(1)
            
