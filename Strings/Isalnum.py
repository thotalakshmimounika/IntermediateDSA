a= ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '#']
c=0
for i in range(len(a)):
    if (ord(a[i])>=65 and ord(a[i])<=90 or ord(a[i])>=97 and ord(a[i])<=122 or ord(a[i])>=48 and ord(a[i])<=57):
        continue
    else:
        print(0)