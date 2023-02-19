# Given a string A of size N, find and return the longest palindromic substring in A.

# Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

# Incase of conflict, return the substring which occurs first ( with the least starting index).



# Problem Constraints
# 1 <= N <= 6000



# Input Format
# First and only argument is a string A.



# Output Format
# Return a string denoting the longest palindromic substring of string A.



# Example Input
# A = "aaaabaaa"


# Example Output
# "aaabaaa"


# Example Explanation
# We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".

def expand(s,p1,p2):
    n=len(s)
    while(p1>=0 and p2<n and s[p1]==s[p2]):
        p1-=1
        p2+=1
    return s[p1+1:p2]
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, s):
        n=len(s)
        ans=''
        for i in range(n):
            c=expand(s,i,i)
            if len(c)>len(ans):
                ans=c
            c=expand(s,i,i+1)
            if len(c)>len(ans):
                ans=c
        return ans