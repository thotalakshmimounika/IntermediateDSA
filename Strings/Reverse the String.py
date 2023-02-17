# You are given a string A of size N.

# Return the string A after reversing the string word by word.

# NOTE:

# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.


# Problem Constraints
# 1 <= N <= 3 * 105



# Input Format
# The only argument given is string A.



# Output Format
# Return the string A after reversing the string word by word.



# Example Input
# Input 1:
#     A = "the sky is blue"
# Input 2:
#     A = "this is ib"


# Example Output
# Output 1:
#     "blue is sky the"
# Output 2:
#     "ib is this"    


# Example Explanation
# Explanation 1:
#     We reverse the string word by word so the string becomes "blue is sky the".
# Explanation 2:
#     We reverse the string word by word so the string becomes "ib is this".

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # Split by space -> list
        ls = A.split()
        # Swapping elements [ex: last ele <-> fast ele]
        p1 = 0
        p2 = len(ls)-1
        while p1 < p2:
            ls[p1], ls[p2] = ls[p2], ls[p1]
            p1 += 1
            p2 -= 1
        # Converting list to string
        return ' '.join(ls)
    

