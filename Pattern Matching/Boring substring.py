# You are given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.

# A boring substring has the following properties:

# Its length is 2.
# Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
# Return 1 if it is possible to rearrange the letters of A such that there are no boring substrings in A else, return 0.



# Problem Constraints
# 1 <= |A| <= 105



# Input Format
# The only argument given is a string A.



# Output Format
# Return 1 if it is possible to rearrange the letters of A such that there are no boring substrings in A else, return 0.



# Example Input
# Input 1:

#  A = "abcd"
# Input 2:

#  A = "aab"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  String A can be rearranged into "cadb" or "bdac" 
# Explanation 2:

#  No arrangement of string A can make it free of boring substrings.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, a):
        a_even=[]
        a_odd=[]
        for i in range(len(a)):
            if ord(a[i])%2==0:
                a_even.append(ord(a[i]))
            else:
                a_odd.append(ord(a[i]))
        a_even.sort()
        a_odd.sort()
        even_smallest=a_even[0]
        even_largest=a_even[-1]
        odd_smallest=a_odd[0]
        odd_largest=a_odd[-1]
        
        if abs(even_smallest-odd_smallest)!=1 or abs(even_smallest-odd_largest)!=1 or abs(even_largest-odd_smallest)!=1 or abs(even_largest-odd_largest)!=1:
            return 1
        return 0
    

#Time Complexity - O(N+NlogN)
#Spacecomplecity - O(N)