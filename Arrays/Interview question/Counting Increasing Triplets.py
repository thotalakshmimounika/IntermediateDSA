# You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]


# Problem Constraints
# 1 <= N <= 103
# 1 <= A[i] <= 109


# Input Format
# First argument A is an array of integers.


# Output Format
# Return an integer.


# Example Input
# Input 1:
# A = [1, 2, 4, 3]
# Input 2:
# A = [2, 1, 2, 3]


# Example Output
# Output 1:
# 2
# Output 2:
# 1


# Example Explanation
# For Input 1:
# The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
# For Input 2:
 
# The triplet that satisfy the conditions is [1, 2, 3].


# Brute force Approach
a = [2, 1, 2, 3]
n=len(a)
s=0
for i in range(n):
    for j in range(i+1,n):
        if a[j]>a[i]:
            for k in range(j+1,n):
                if a[k]>a[j]:
                    s+=1
print(s)
# time complexity - O(n^3)
# space complexity - O(1)

# Optimised sol
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=len(a)
        s=0
        ans=0
        for j in range(1,n):
            scount=0
            for i in range(j-1,-1,-1):
                if a[i]<a[j]:
                    scount+=1
            lcount=0
            for k in range(j+1,n):
                if a[k]>a[j]:
                    lcount+=1
            ans+=scount*lcount
        return ans

# time complexity - O(n^2)
# space complexity - O(1)