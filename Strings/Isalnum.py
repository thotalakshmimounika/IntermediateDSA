# You are given a function isalpha() consisting of a character array A.

# Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.



# Problem Constraints
# 1 <= |A| <= 105



# Input Format
# Only argument is a character array A.



# Output Format
# Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.



# Example Input
# Input 1:

#  A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
# Input 2:

#  A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  All the characters are alphanumeric.
# Explanation 2:

#  All the characters are NOT alphabets i.e ('#').

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, a):
        c=0
        for i in range(len(a)):
            if (ord(a[i])>=65 and ord(a[i])<=90 or ord(a[i])>=97 and ord(a[i])<=122 or ord(a[i])>=48 and ord(a[i])<=57):
                c+=1
        if c==len(a):
            return 1
        return 0
        

#or
class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, a):
        c=0
        for i in a:
            if not i.isalnum():
                return 0
        return 1
