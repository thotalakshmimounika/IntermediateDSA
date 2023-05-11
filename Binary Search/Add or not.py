# Given an array of integers A of size N and an integer B.

# In a single operation, any one element of the array can be increased by 1. You are allowed to do at most B such operations.

# Find the number with the maximum number of occurrences and return an array C of size 2, where C[0] is the number of occurrences, and C[1] is the number with maximum occurrence.
# If there are several such numbers, your task is to find the minimum one.



# Problem Constraints
# 1 <= N <= 105

# -109 <= A[i] <= 109

# 0 <= B <= 109



# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.



# Output Format
# Return an array C of size 2, where C[0] is number of occurence and C[1] is the number with maximum occurence.



# Example Input
# Input 1:

#  A = [3, 1, 2, 2, 1]
#  B = 3
# Input 2:

#  A = [5, 5, 5]
#  B = 3


# Example Output
# Output 1:

#  [4, 2]
# Output 2:

#  [3, 5]


# Example Explanation
# Explanation 1:

#  Apply operations on A[2] and A[4]
#  A = [3, 2, 2, 2, 2]
#  Maximum occurence =  4
#  Minimum value of element with maximum occurence = 2
# Explanation 2:

#  A = [5, 5, 5]
#  Maximum occurence =  3
#  Minimum value of element with maximum occurence = 5

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, a,b):
        n=len(a)
        res=[]
        a.sort()
        occ=1
        res=[0,0]
        pf=[0]*(n+1)
        pf[1]=a[0]
        for i in range(2,n+1):
            pf[i]=pf[i-1]+a[i-1]
        for i in range(n):
            left=1
            right=i+1
            while(left<=right):
                mid=(left+right)//2
                operations=(a[i]*mid) -(pf[i+1]-pf[i+1 - (mid)])
                if operations<=b:
                    occ=mid
                    left=mid+1
                else:
                    right=mid-1
            if occ>res[0]:
                res[0]=occ
                res[1]=a[i]
        return res

#Time complexity - O(nlogn)
#Space complecity - O(n)