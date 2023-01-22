a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n=len(a)
ans=[[0]*len(a) for _ in range(2*len(a)-1)]
r=-1
c=-1
for i in range(n):
     s_r=0
     s_c=i
     r+=1
     c=0
     while(s_r<n and s_c>=0):
          ans[r][c]=a[s_r][s_c]
          s_r+=1
          s_c-=1
          c+=1
r=n-1
c=0
for i in range(1,n):
     s_r=i
     s_c=n-1
     r+=1
     c=0
     while(s_r<n and s_c>=0):
          ans[r][c]=a[s_r][s_c]
          s_r+=1
          s_c-=1
          c+=1
print(ans)