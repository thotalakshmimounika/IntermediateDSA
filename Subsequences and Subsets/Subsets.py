a = [1, 2, 3]
n=len(a)
s=[]
for i in range(0,2**n):
    for j in range(n):
        if i &(1<<j)!=0:
            s.append(a[i])
print(s)