a= [1, 0, 1, 0, 1]
b= 1 
n=len(a)
s=2*b+1
k=[]
for i in range(n):
    p=a[i] 
    c=0
    for j in range(i,min(i+s,n)):
        if a[j]==p:
            p=1-p
            c+=1
        if c==s:
            k.append(int((i+j)/2))
print(k)
Or 

a=[ 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1 ]
b=0
n = len(a)
s=2*b+1
ans = []
c=0
p=a[0]
for i in range(n):
        if p==a[i]:
                c=1
                continue
        else:
                p=1-p
                c+=1
                if c%s==0:
                        ans.append(i-b)
                        c-=1
print(ans)




















#class Solution:
 #   def __init__(self):
 #       self.n = 2
  #      self.create()

  #  def create(self):
   #     self.n = self.n*2

#s = Solution()
#r = Solution
#print(r)
#s.create()
#s.push()
#print(s.n)

