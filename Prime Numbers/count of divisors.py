a = [ 20, 39, 29, 51, 96, 32, 35, 50, 57, 7, 59, 51, 85, 55, 8, 26, 15, 4, 4, 18, 32, 49, 40, 46, 83, 77, 100, 92 ]

n=len(a)
cf=[1]*(max(a)+1)
for i in range(2,(len(cf))):
    for j in range(i,len(cf),i):
        cf[j]+=1
ans=[]
for i in range(n):
    a[i]=cf[a[i]]
print(a)

