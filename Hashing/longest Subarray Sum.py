# Given an array A of N integers.

# Find the length of the longest subarray in the array which sums to zero.


# Problem Constraints
# 1 <= N <= 105
# -109 <= A[i] <= 109


# Input Format
# Single argument which is an integer array A.


# Output Format
# Return an integer.


# Example Input
# Input 1:

#  A = [1, -2, 1, 2]
# Input 2:

#  A = [3, 2, -1]


# Example Output
# Output 1:

# 3
# Output 2:

# 0


# Example Explanation
# Explanation 1:

#  [1, -2, 1] is the largest subarray which sums up to 0.
# Explanation 2:

#  No subarray sums up to 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=len(a)
        pf=[0]*n
        pf[0]=a[0]

        for i in range(1,n):
            pf[i]=pf[i-1]+a[i]
        
        indect={}
        ans=0
        for i in range(n):
            if pf[i]==0:
                ans=max(ans,i+1)
            elif pf[i] in indect:
                ans=max(ans,i-indect[pf[i]])
            else:
                indect[pf[i]]=i
        return ans
    
# Time complexity - O(N+N)~O(N) -> N is len(A)
#Space Complexity - O(N+N)~O(N)