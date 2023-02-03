a=11
c=0
while(a>0):
    if a&1==1:
        c+=1
        a=a>>1
    else:
        a=a>>1
print(c)