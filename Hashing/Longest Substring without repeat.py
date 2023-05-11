# Given a string A, find the length of the longest substring without repeating characters.

# Note: Users are expected to solve in O(N) time complexity.



# Problem Constraints
# 1 <= size(A) <= 106

# String consists of lowerCase,upperCase characters and digits are also present in the string A.



# Input Format
# Single Argument representing string A.



# Output Format
# Return an integer denoting the maximum possible length of substring without repeating characters.



# Example Input
# Input 1:

#  A = "abcabcbb"
# Input 2:

#  A = "AaaA"


# Example Output
# Output 1:

#  3
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Substring "abc" is the longest substring without repeating characters in string A.
# Explanation 2:

#  Substring "Aa" or "aA" is the longest substring without repeating characters in string A.
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, a):
        n=len(a)
        s=set()
        l,r=0,0
        ans=0
        while(r<n):
            if a[r] in s:
                s.remove(a[l])
                l+=1
            else:
                s.add(a[r])
                ans=max(ans,(r-l+1))
                r+=1
        return ans
