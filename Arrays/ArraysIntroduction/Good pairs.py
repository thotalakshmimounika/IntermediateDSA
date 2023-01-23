a=[1,4,2,3]
b=7
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==b:
            print(1)

