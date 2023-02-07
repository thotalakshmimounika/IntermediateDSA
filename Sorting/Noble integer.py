a = [1, 1, 3, 3]
a.sort(reverse=True)
n=len(a)
p=0
for i in range(n):
    if a[i]==a[i-1]:
        if p==a[i]:
            print(1)
    else:
        p=i
        if p==a[i]:
            print(1)
print(-1)





