# Given two strings A and B, determine if they are isomorphic.

# A and B are called isomorphic strings if all occurrences of each character in A can be replaced with another character to get B and vice-versa.



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= |B| <= 100000

# A and B contain only lowercase characters.



# Input Format
# The first Argument is string A.

# The second Argument is string B.



# Output Format
# Return 1 if strings are isomorphic, 0 otherwise.



# Example Input
# Input 1:

# A = "aba"
# B = "xyx"
# Input 2:

# A = "cvv"
# B = "xyx"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Replace 'a' with 'x', 'b' with 'y'.
# Explanation 2:

#  A cannot be converted to B.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, a,b):
        if len(a)!=len(b):
            return 0
        d1={}
        n=len(a)
        for i in a:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        d2={}
        for j in b:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
        for i in range(n):
            if d1[a[i]]!=d2[b[i]]:
                return 0
        return 1
