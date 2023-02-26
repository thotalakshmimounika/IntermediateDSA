a=[16,3,3,6,7,8,17,13,7]

m=1
l=1
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        l+=1
    else:
        if m<l:
            m=l
        l=1
if m<l:
    m=l
print(m)