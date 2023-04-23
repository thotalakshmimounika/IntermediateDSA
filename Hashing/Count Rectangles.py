# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.

# Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.



# Problem Constraints
# 1 <= N <= 2000
# 0 <= A[i], B[i] <= 109



# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer array B.



# Output Format
# Return the number of unordered quadruplets that form a rectangle.



# Example Input
# Input 1:

#  A = [1, 1, 2, 2]
#  B = [1, 2, 1, 2]
# Input 1:

#  A = [1, 1, 2, 2, 3, 3]
#  B = [1, 2, 1, 2, 1, 2]


# Example Output
# Output 1:

#  1
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  All four given points make a rectangle. So, the answer is 1.
# Explanation 2:

#  3 quadruplets which make a rectangle are: (1, 1), (2, 1), (2, 2), (1, 2)
#                                            (1, 1), (3, 1), (3, 2), (1, 2)
#                                            (2, 1), (3, 1), (3, 2), (2, 2)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        s=set()
        for i in range(n):
            s.add((a[i],b[i]))
        ans=0
        for i in range(n):
            x1,y1=a[i],b[i]
            for j in range(i+1,n):
                x2,y2=a[j],b[j]
                if x1!=x2 and y1!=y2:
                    if (x1,y2) in s and (x2,y1) in s:
                        ans+=1
        return ans//2
#Time complexity - O(N^2)
#Space complexity - O(N)