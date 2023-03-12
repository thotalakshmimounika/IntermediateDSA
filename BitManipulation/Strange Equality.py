a=5
for i in range(a-1,-1,-1):
    if i+a == a^i:
        a1=i
        break
i=a+1
while(i>a):
    if i+a == a^i:
        a2=i
        break
    i+=1
print(a1^a2)