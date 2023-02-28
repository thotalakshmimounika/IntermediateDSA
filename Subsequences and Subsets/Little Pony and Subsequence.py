a= "djjhibvetj"
s=''
min=a[0]
for i in range(1,len(a)-1):
    if a[i]<min:
        min=a[i]
s=s+min
a=a.replace(min,'',1)
min1=a[0]
for i in range(1,len(a)):
    if a[i]<min1:
        min1=a[i]
s=s+min1
print(s)