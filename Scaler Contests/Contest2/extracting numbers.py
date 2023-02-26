#Given a string A. The string contains alphanumeric characters.Find the sum of all numbers present in it.
a="a12b34c"
k="0"
s=0
for i in range(len(a)):
    if a[i].isdigit():
        k=k+a[i]
    else:
        s+=int(k)
        k="0"
print(s+int(k))