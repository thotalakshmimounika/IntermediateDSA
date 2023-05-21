a=[3,2,1,4,1,5]
b=5
from collections import deque
n=len(a)
q=deque()
s,c=0,0
for i in a:
    if len(q)==0:
        q.append(i)
        s+=q[-1]
        if s==b:
            c+=1
    else:
        q.append(i)
        s+=q[-1]
        if s==b:
            c+=1
        elif s>b:
            while q and s>b:
                x=q.popleft()
                s-=x
                if s==b:
                    c+=1
print(c)
                
                    
                
                    
        
