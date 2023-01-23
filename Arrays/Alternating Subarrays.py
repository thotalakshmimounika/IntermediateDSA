# You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

# You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

# A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.



# Problem Constraints
# 1 <= N <= 103

# A[i] equals to 0 or 1.

# 0 <= B <= (N - 1) / 2



# Input Format
# First argument is an integer array A.

# Second argument is an integer B.



# Output Format
# Return an integer array containing indices(0-based) in sorted order. If no such index exists, return an empty integer array.



# Example Input
# Input 1:

#  A = [1, 0, 1, 0, 1]
#  B = 1 
# Input 2:

#  A = [0, 0, 0, 1, 1, 0, 1]
#  B = 0 


# Example Output
# Output 1:

#  [1, 2, 3]
# Output 2:

#  [0, 1, 2, 3, 4, 5, 6]


# Example Explanation
# Explanation 1:

#  Index 1 acts as a centre of alternating sequence: [A0, A1, A2]
#  Index 2 acts as a centre of alternating sequence: [A1, A2, A3]
#  Index 3 acts as a centre of alternating sequence: [A2, A3, A4] 
# Explanation 2:

#  Each index in the array acts as the center of alternating sequences of lengths 1.
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

#time Complexity - O(n^2)
#Space complexity - O(n)
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

#time Complexity - O(n)
#Space complexity - O(n)



















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

