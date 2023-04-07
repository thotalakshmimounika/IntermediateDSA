# Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

# NOTE: Users are expected to solve this in O(log(N)) time.



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= A[i] <= 10^9



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return the single element that appears only once.



# Example Input
# Input 1:

# A = [1, 1, 7]
# Input 2:

# A = [2, 3, 3]


# Example Output
# Output 1:

#  7
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  7 appears once
# Explanation 2:

#  2 appears once
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=len(a)
        if n==1:
            return a[0]
        if a[0]!=a[1]:
            return a[0]
        if a[n-1]!=a[n-2]:
            return a[n-1]
        left=2
        right=n-3
        while(left<=right):
            mid=(left+right)//2
            if a[mid-1]!=a[mid] and a[mid]!=a[mid+1]:
                return a[mid]
            fo=mid
            if a[mid]==a[mid-1]:
                fo=mid-1
            if fo%2==0:
                left=fo+2
            else:
                right=fo-1
        

#Time complexity - O(logn base 2)
#space complexity - O(1)