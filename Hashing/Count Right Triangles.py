# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

# Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

# NOTE: The answer may be large so return the answer modulo (109 + 7).



# Problem Constraints
# 1 <= N <= 105

# 0 <= A[i], B[i] <= 109



# Input Format
# The first argument given is an integer array A.
# The second argument given is the integer array B.



# Output Format
# Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).



# Example Input
# Input 1:

#  A = [1, 1, 2]
#  B = [1, 2, 1]
# Input 2:

#  A = [1, 1, 2, 3, 3]
#  B = [1, 2, 1, 2, 1]


# Example Output
# Output 1:

#  1
# Output 2:

#  6


# Example Explanation
# Explanation 1:

#  All three points make a right angled triangle. So return 1.
# Explanation 2:

#  6 triplets which make a right angled triangle are:    (1, 1), (1, 2), (2, 1)
#                                                        (1, 1), (3, 1), (1, 2)
#                                                        (1, 1), (3, 1), (3, 2)
#                                                        (2, 1), (3, 1), (3, 2)
#                                                        (1, 1), (1, 2), (3, 2)
#                                                        (1, 2), (3, 1), (3, 2)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        hm1={}
        hm2={}
        m=10**9 + 7
        for i in a:
            if i in hm1:
                hm1[i]+=1
            else:
                hm1[i]=1
        for i in b:
            if i in hm2:
                hm2[i]+=1
            else:
                hm2[i]=1
        ans=0
        for i in range(n):
            if a[i] in hm1:
                xcordcount=hm1[a[i]]-1
            if b[i] in hm2:
                ycordcount=hm2[b[i]]-1
            ans= (ans%m + ((xcordcount)%m*(ycordcount)%m)%m)%m
        return ans%m

#Time complexity - O(N)
#Space Complexity - O(N)