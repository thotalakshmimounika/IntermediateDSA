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

