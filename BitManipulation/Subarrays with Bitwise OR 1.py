a=5
b=[ 0, 1, 0, 0, 0 ]
totalSubarrays= int((a*(a+1))/2)
print(totalSubarrays)
c=0
s=0
for i in b:
    if i==0:
        c+=1
    else:
        s+=int((c*(c+1))/2)
        c=0
if c>=1:
        s+=int((c*(c+1))/2)

print(totalSubarrays -s)
