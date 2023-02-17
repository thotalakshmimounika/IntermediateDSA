# Given a string A, you are asked to reverse the string and return the reversed string.



# Problem Constraints
# 1 <= |A| <= 105

# String A consist only of lowercase characters.



# Input Format
# First and only argument is a string A.



# Output Format
# Return a string denoting the reversed string.



# Example Input
# Input 1:

#  A = "scaler"
# Input 2:

#  A = "academy"


# Example Output
# Output 1:

#  "relacs"
# Output 2:

#  "ymedaca"


# Example Explanation
# Explanation 1:

#  Reverse the given string.
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        a="".join(reversed(a))
        return a
#or
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        return "".join(reversed(a))
#or
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        s=""
        for i in a:
            s=i+s
        return s


