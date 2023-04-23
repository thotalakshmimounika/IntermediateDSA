# Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B in linear time complexity.
# Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

# Note:

# If there is no such window in A that covers all characters in B, return the empty string.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index and length )


# Problem Constraints
# 1 <= size(A), size(B) <= 106



# Input Format
# The first argument is a string A.
# The second argument is a string B.



# Output Format
# Return a string denoting the minimum window.



# Example Input
# Input 1:

#  A = "ADOBECODEBANC"
#  B = "ABC"
# Input 2:

#  A = "Aa91b"
#  B = "ab"


# Example Output
# Output 1:

#  "BANC"
# Output 2:

#  "a91b"


# Example Explanation
# Explanation 1:

#  "BANC" is a substring of A which contains all characters of B.
# Explanation 2:

#  "a91b" is the substring of A which contains all characters of B.

from collections import Counter
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, a,b):
        n=len(b)
        m=len(a)
        hmb = Counter(b)
        s,e=0,0
        cnt=n
        ans=m
        flag=False
        while(e<m):
            if a[e] in hmb:
                hmb[a[e]]-=1
                if hmb[a[e]]>=0:
                    cnt-=1
            e+=1
            if cnt>0:
                continue
            while(cnt==0):
                if a[s] in hmb:
                    hmb[a[s]]+=1
                    if hmb[a[s]]>0:
                        cnt+=1
                s+=1
            if (e-s)<ans:
                flag=True
                start=s
                end=e
                ans=e-s



        if flag==True:
            if start==1:
                a[start:end]
            return a[start-1:end]
        return ""
                
#TC - O(N+M)
#SC- O(N)