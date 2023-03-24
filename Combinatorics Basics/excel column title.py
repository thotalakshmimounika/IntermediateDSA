# Given a positive integer A, return its corresponding column title as it appears in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 


# Problem Constraints
# 1 <= A <= 109



# Input Format
# First and only argument of input contains single integer A



# Output Format
# Return a string denoting the corresponding title.



# Example Input
# Input 1:

# A = 3
# Input 2:

 
# A = 27


# Example Output
# Output 1:

# "C"
# Output 2:

# "AA"


# Example Explanation
# Explanation 1:

 
# 3 corrseponds to C.
# Explanation 2:

#     1 -> A,
#     2 -> B,
#     3 -> C,
#     ...
#     26 -> Z,
#     27 -> AA,
#     28 -> AB 

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, a):
        ans=""
        while(a>0):
            if a%26==0:
                a=(a//26)-1
                r=26
            else:
                r=a%26
                a=a//26
            ans+=chr(64+r)
        return ans[::-1]
    
#Time complexity - logA base-26
#space complexity - O(1)