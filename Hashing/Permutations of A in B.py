# You are given two strings, A and B, of size N and M, respectively.

# You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



# Problem Constraints
# 1 <= N < M <= 105



# Input Format
# Given two arguments, A and B of type String.



# Output Format
# Return a single integer, i.e., number of permutations of A present in B as a substring.



# Example Input
# Input 1:

#  A = "abc"
#  B = "abcbacabc"
# Input 2:

#  A = "aca"
#  B = "acaa"


# Example Output
# Output 1:

#  5
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Permutations of A that are present in B as substring are:
#     1. abc
#     2. cba
#     3. bac
#     4. cab
#     5. abc
#     So ans is 5.
# Explanation 2:

#  Permutations of A that are present in B as substring are:
#     1. aca
#     2. caa 
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        m=len(b)
        hma={}
        for i in a:
            if i in hma:
                hma[i]+=1
            else:
                hma[i]=1
        hmb={}
        for i in range(n):
            if b[i] in hmb:
                hmb[b[i]]+=1
            else:
                hmb[b[i]]=1
        s=0
        e=n-1
        ans=0
        while(e<m):
            if hma==hmb:
                ans+=1

            if hmb[b[s]]>1:
                hmb[b[s]]-=1
            else:
                del hmb[b[s]]
            s+=1
            e+=1
            if e>=m:
                break
            if b[e] in hmb:
                hmb[b[e]]+=1
            else:
                hmb[b[e]]=1
        return ans
            
#Tc - O(N+M)
#Sc - O(1)