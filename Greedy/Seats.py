a=  ".x.x.x..x"
m=10**9+7
people=[]
for i in range(len(a)):
    if a[i]=='x':
        people.append(i)
ans=0
if len(people)==0 or len(people)==1:
    print(0)
median=len(people)//2
k=people[median]
for i in range(len(people)):
    ans+=(abs(people[i]-k) - abs(median-i))%m
print(ans)







