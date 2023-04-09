# Given a sorted array of integers A of size N and an integer B.

# array A is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

# You are given a target value B to search. If found in the array, return its index otherwise, return -1.

# You may assume no duplicate exists in the array.

# NOTE: Users are expected to solve this in O(log(N)) time.



# Problem Constraints
# 1 <= N <= 1000000

# 1 <= A[i] <= 109

# all elements in A are distinct.



# Input Format
# The first argument given is the integer array A.

# The second argument given is the integer B.



# Output Format
# Return index of B in array A, otherwise return -1



# Example Input
# Input 1:

# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4 
# Input 2:

# A : [ 9, 10, 3, 5, 6, 8 ]
# B : 5


# Example Output
# Output 1:

#  0 
# Output 2:

#  3


# Example Explanation
# Explanation 1:

# Target 4 is found at index 0 in A. 
# Explanation 2:

# Target 5 is found at index 3 in A.
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, a,b):
        a=list(a)
        n=len(a)
        left=0
        right=n-1
        while(left<=right):
            mid=(left+right)//2
            if a[mid]==b:
                return mid
            elif a[mid]>=a[left]:
                if a[mid]>=b and a[left]<=b:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if a[mid]<=b and a[right]<b:
                    right=mid-1
                else:
                    left=mid+1


        return -1

#Time complexity - O(logn)
#Space complexity - O(1)