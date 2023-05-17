# Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

# Find the largest rectangle containing only 1's and return its area.

# Note: Rows are numbered from top to bottom and columns are numbered from left to right.


# Input Format

# The only argument given is the integer matrix A.
# Output Format

# Return the area of the largest rectangle containing only 1's.
# Constraints

# 1 <= N, M <= 1000
# 0 <= A[i] <= 1
# For Example

# Input 1:
#     A = [   [0, 0, 1]
#             [0, 1, 1]
#             [1, 1, 1]   ]
# Output 1:
#     4

# Input 2:
#     A = [   [0, 1, 0, 1]
#             [1, 0, 1, 0]    ]
# Output 2:
#     1

def leftsmallest(a):
    l=len(a)
    stack=[]
    nls=[-1]*l
    for i in range(l):
        while(len(stack)!=0 and a[stack[-1]]>=a[i]):
            stack.pop()
        if len(stack)!=0:
            nls[i]=stack[-1]
        stack.append(i)
    stack.clear()
    return nls

def rightsmallest(a):
    m=len(a)
    stack=[]
    nrs=[m]*m
    for i in range(m-1,-1,-1):
        while(len(stack)!=0 and a[stack[-1]]>=a[i]):
            stack.pop()
        if len(stack)!=0:
            nrs[i]=stack[-1]
        stack.append(i)
    stack.clear()
    return nrs

def largestRectangleArea(a):
    ans=float('-inf')
    nlsmall=leftsmallest(a)
    nrsmall=rightsmallest(a)
    for i in range(len(a)):
        area=a[i]*(nrsmall[i]-nlsmall[i]-1)
        ans=max(ans,area)
    return ans
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        m=len(A[0])

        currrow=A[0]
        maxarea=largestRectangleArea(currrow)

        for i in range(1,n):
            for j in range(m):
                if A[i][j]==1:
                    currrow[j]+=1
                else:
                    currrow[j]=0
            maxarea=max(maxarea,largestRectangleArea(currrow))
        return maxarea
        

