# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



# Problem Constraints
# 1 <= |A| <= 100000



# Input Format
# First and only argument is the vector A



# Output Format
# Return one integer, the answer to the question



# Example Input
# Input 1:

# A = [0, 1, 0, 2]
# Input 2:

# A = [1, 2]


# Example Output
# Output 1:

# 1
# Output 2:

# 0


# Example Explanation
# Explanation 1:

# 1 unit is trapped on top of the 3rd element.
# Explanation 2:

# No water is trapped.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, a):
        n=len(a)
        p=[0]*n
        s=[0]*n

        p[0]=a[0]
        s[n-1]=a[n-1]

        for i in range(1,n):
            p[i]=max(p[i-1],a[i])
        for i in range(n-2,-1,-1):
            s[i]=max(s[i+1],a[i])
        t=0
        for i in range(n):
            t+=min(p[i],s[i])-a[i]
        return t

#Time complexity - O(N)
#space Complexity - O(2N)

        
        
