# Given a matrix of integers A of size N x M in which each row is sorted.

# Find and return the overall median of matrix A.

# NOTE: No extra memory is allowed.

# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



# Problem Constraints
# 1 <= N, M <= 10^5

# 1 <= N*M <= 10^6

# 1 <= A[i] <= 10^9

# N*M is odd



# Input Format
# The first and only argument given is the integer matrix A.



# Output Format
# Return the overall median of matrix A.



# Example Input
# Input 1:

# A = [   [1, 3, 5],
#         [2, 6, 9],
#         [3, 6, 9]   ] 
# Input 2:

# A = [   [5, 17, 100]    ]


# Example Output
# Output 1:

#  5 
# Output 2:

#  17


# Example Explanation
# Explanation 1:

# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
# Median is 5. So, we return 5. 
# Explanation 2:

# Median is 17.

def countofsmallerelements(mid,a):
    l,r=0,len(a)-1
    while(l<=r):
        m=(l+r)//2
        if a[m]<=mid:
            l=m+1
        else:
            r=m-1
    return l
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, a):
        n=len(a)
        m=len(a[0])
        minele=float('inf')
        maxele=float('-inf')
        for i in range(n):
            if a[i][0]<minele:
                minele=a[i][0]
            if a[i][m-1]>maxele:
                maxele=a[i][m-1]                
        left,right=minele,maxele

        while(left<=right):
            mid=(left+right)//2
            x=0
            for i in range(n):
                x+=countofsmallerelements(mid,a[i])
            if x<=(n*m)/2:
                left=mid+1
            else:
                right=mid-1
        return left

#Time complexity - O(N+Nlog(NM))
#Space Complexity - O(1)