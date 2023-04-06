# Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.


# Problem Constraints
# 1 <= |A| <= 105
# 1 <= A[i] <= 105


# Input Format
# The first argument is an integer array A.


# Output Format
# Return an integer array that is the sorted array A.


# Example Input
# Input 1:
# A = [1, 3, 1]
# Input 2:
# A = [4, 2, 1, 3]


# Example Output
# Output 1:
# [1, 1, 3]
# Output 2:
# [1, 2, 3, 4]


# Example Explanation
# For Input 1:
# The array in sorted order is [1, 1, 3].
# For Input 2:
# The array in sorted order is [1, 2, 3, 4].

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, a):
        n=len(a)
        m=max(a)
        fa=[0]*(m+1)
        p=[0]*(m+1)
        for i in range(n): #frequency array
            fa[a[i]]+=1
        for i in range(1,m+1):  #prefix Sum array which tells there are x elements until that index which gives stable dorting
            p[i]=p[i-1]+fa[i]
        ans=[0]*(n)
        for i in range(n-1,-1,-1): # iterate over the original array from right to left and store the element in ans array with correct index based on prefix sum array
            val=p[a[i]]
            ans[val-1]=a[i]
            p[a[i]]-=1
        for i in range(n): # store the sorted array back to original array
            a[i]=ans[i]
        return a

#Time complexity - O(4N+R)
#Space complexity - O(N+R)