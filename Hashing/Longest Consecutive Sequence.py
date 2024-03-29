# Given an unsorted integer array A of size N.

# Find the length of the longest set of consecutive elements from array A.



# Problem Constraints
# 1 <= N <= 106

# -106 <= A[i] <= 106



# Input Format
# First argument is an integer array A of size N.



# Output Format
# Return an integer denoting the length of the longest set of consecutive elements from the array A.



# Example Input
# Input 1:

# A = [100, 4, 200, 1, 3, 2]
# Input 2:

# A = [2, 1]


# Example Output
# Output 1:

#  4
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  The set of consecutive elements will be [1, 2, 3, 4].
# Explanation 2:

#  The set of consecutive elements will be [1, 2].

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, a):
        k=set(a)
        ans=float('-inf')
        for i in k:
            if i-1 not in k:
                c=1
                x=i+1
                while x in k:
                    c+=1
                    x+=1
                ans=max(ans,c)
        return ans

#Storing the unique elements in set first
#Iterate over the set - Checking if element-1 is present in set or not
#If not that element can be our first element
#check for next consecutive elements and then count its length
                
#Time complexity - O(N)
#space complexity - O(1)
