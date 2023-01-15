a = [2, 4, 1, 3, 2]
h=a[0]
ind=0
for i in range(1,len(a)):
    if h<a[i]:
        h=a[i]
        ind=i
d=0
for i in range(len(a)):
    if i!=ind:
        d=d+(h-a[i])
print(d)
