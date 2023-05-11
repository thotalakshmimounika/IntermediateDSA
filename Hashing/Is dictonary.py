# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



# Problem Constraints
# 1 <= N, length of each word <= 105

# Sum of the length of all words <= 2 * 106



# Input Format
# The first argument is a string array A of size N.

# The second argument is a string B of size 26, denoting the order.



# Output Format
# Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



# Example Input
# Input 1:

#  A = ["hello", "scaler", "interviewbit"]
#  B = "adhbcfegskjlponmirqtxwuvzy"
# Input 2:

#  A = ["fine", "none", "no"]
#  B = "qwertyuiopasdfghjklzxcvbnm"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  The order shown in string B is: h < s < i for the given words. So return 1.
# Explanation 2:

#  "none" should be present after "no". Return 0.
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        d={}
        for i in range(26):
            d[b[i]]=i
        for i in range(n-1):
            word1,word2=a[i],a[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    if d[word1[j]]>d[word2[j]]:
                        return 0
                    else:
                        break
            else:
                if len(word1)>len(word2):
                    return 0
        return 1