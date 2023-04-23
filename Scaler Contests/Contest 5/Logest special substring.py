a="rishabhkejariwal"
b=[0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]
c=2
n=len(a)
res=0
i,j,s=0,0,0
for i in range(n):
    val=ord(a[i])-97
    if b[val]==1:
        s+=1
    if s<=c:
        res=max(res,i-j+1)
    else:
        while(s>c):
            if b[ord(a[j])-97]==1:
                s-=1
            j+=1
print(res)      
                
                
                
            
        
            
            
            
                