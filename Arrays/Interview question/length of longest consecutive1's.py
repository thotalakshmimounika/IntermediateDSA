# Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


# Input Format

# The only argument given is string A.
# Output Format

# Return the length of the longest consecutive 1’s that can be achieved.
# Constraints

# 1 <= length of string <= 1000000
# A contains only characters 0 and 1.
# For Example

# Input 1:
#     A = "111000"
# Output 1:
#     3

# Input 2:
#     A = "111011101"
# Output 2:
#     7

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, a):
        a = [int(x) for x in a]
        n=len(a)
        c=0
        for l in range(n):
            if a[l]==1:
                c+=1
            if n==c:
                return n
        ans=0
        for j in range(n):
            if a[j]==0:
                i=j-1
                ls=0
                while(i>=0 and a[i]==1):
                    ls+=1
                    i-=1
                i=j+1
                rs=0
                while(i<n and a[i]==1):
                    rs+=1
                    i+=1
                if ls+rs==c:
                    ans=max(c,ls+rs)
                else:
                    ans=max(ans,ls+rs+1)
               
        return ans

#time complexity - O(N)
#Space complexity - O(1)