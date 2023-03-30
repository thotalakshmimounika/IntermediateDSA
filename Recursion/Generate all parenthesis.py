# Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.



# Problem Constraints
# 1 <= A <= 10



# Input Format
# First and only argument is integer A.



# Output Format
# Return a sorted list of all possible parenthesis.



# Example Input
# Input 1:

# A = 3
# Input 2:

# A = 1


# Example Output
# Output 1:

# [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
# Output 2:

# [ "()" ]


# Example Explanation
# Explanation 1:

#  All paranthesis are given in the output list.
# Explanation 2:

#  All paranthesis are given in the output list.

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, a):
        ans=[]
        def Parenthesis(n,opening,closing,s):
            if opening==closing==n:
                ans.append(s)
                return
            if opening<n:
                Parenthesis(n,opening+1,closing,s+"(")
            if closing<opening:
                Parenthesis(n,opening,closing+1,s+")")
        Parenthesis(a,0,0,"")
        return ans
