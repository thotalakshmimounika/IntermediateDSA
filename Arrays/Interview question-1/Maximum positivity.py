a= [5, 6, -1, 7, 8]
n=len(a)
c=[]
for i in range(n):
    if a[i]<0:
        continue
    for j in range(i+1,n):
        if a[j]<0:
            break
        else:
            c.append(a[i])
print(c)
