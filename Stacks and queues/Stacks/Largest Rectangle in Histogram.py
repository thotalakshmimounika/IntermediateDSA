# Given an array of integers A.

# A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

# Find the area of the largest rectangle formed by the histogram.



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= A[i] <= 1000000000



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return the area of the largest rectangle in the histogram.



# Example Input
# Input 1:

#  A = [2, 1, 5, 6, 2, 3]
# Input 2:

#  A = [2]


# Example Output
# Output 1:

#  10
# Output 2:

#  2


# Example Explanation
# Explanation 1:

# The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
# Explanation 2:

# Largest rectangle has area 2.

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, a):
        n=len(a)
        stack=[]
        nlsmall=[-1]*n
        for i in range(n):
            while(len(stack)!=0 and a[stack[-1]]>=a[i]):
                stack.pop()
            if len(stack)!=0:
                nlsmall[i]=stack[-1]
            stack.append(i)
        stack.clear()
        nrsmall=[n]*n
        for i in range(n-1,-1,-1):
            while(len(stack)!=0 and a[stack[-1]]>=a[i]):
                stack.pop()
            if len(stack)!=0:
                nrsmall[i]=stack[-1]
            stack.append(i)
        stack.clear()

        ans=float('-inf')
        for i in range(n):
            area=a[i]*(nrsmall[i]-nlsmall[i]-1)
            ans=max(ans,area)
        return ans

        
