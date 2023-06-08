# Given an array of integers A.

# The value of an array is computed as the difference between the maximum element in the array and the minimum element in the array A.

# Calculate and return the sum of values of all possible subarrays of A modulo 109+7.



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= A[i] <= 1000000



# Input Format
# The first and only argument given is the integer array A.



# Output Format
# Return the sum of values of all possible subarrays of A modulo 109+7.



# Example Input
# Input 1:

#  A = [1]
# Input 2:

#  A = [4, 7, 3, 8]


# Example Output
# Output 1:

#  0
# Output 2:

#  26


# Example Explanation
# Explanation 1:

# Only 1 subarray exists. Its value is 0.
# Explanation 2:

# value ( [4] ) = 4 - 4 = 0
# value ( [7] ) = 7 - 7 = 0
# value ( [3] ) = 3 - 3 = 0
# value ( [8] ) = 8 - 8 = 0
# value ( [4, 7] ) = 7 - 4 = 3
# value ( [7, 3] ) = 7 - 3 = 4
# value ( [3, 8] ) = 8 - 3 = 5
# value ( [4, 7, 3] ) = 7 - 3 = 4
# value ( [7, 3, 8] ) = 8 - 3 = 5
# value ( [4, 7, 3, 8] ) = 8 - 3 = 5
# sum of values % 10^9+7 = 26

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        mod = 10**9 + 7
        n = len(a)
        stack=[]
        nlsmall=[-1]*n
        for i in range(n):
            while(len(stack)!=0 and a[stack[-1]]>=a[i]):
                stack.pop()
            if len(stack)!=0:
                nlsmall[i]=stack[-1]
            stack.append(i)
        stack.clear()

        nrsmall=[n]*n
        for i in range(n-1,-1,-1):
            while(len(stack)!=0 and a[stack[-1]]>=a[i]):
                stack.pop()
            if len(stack)!=0:
                nrsmall[i]=stack[-1]
            stack.append(i)
        stack.clear()

        nlgreat=[-1]*n
        for i in range(n):
            while(len(stack)!=0 and a[stack[-1]]<=a[i]):
                stack.pop()
            if len(stack)!=0:
                nlgreat[i]=stack[-1]
            stack.append(i)
        stack.clear()

        nrgreat=[n]*n
        for i in range(n-1,-1,-1):
            while(len(stack)!=0 and a[stack[-1]]<=a[i]):
                stack.pop()
            if len(stack)!=0:
                nrgreat[i]=stack[-1]
            stack.append(i)
        stack.clear()

        maxs,mins=0,0
        for i in range(n):
            maxs+=a[i]*(i-nlgreat[i])*(nrgreat[i]-i)
        for i in range(n):
            mins+=a[i]*(i-nlsmall[i])*(nrsmall[i]-i)
        return (maxs-mins)%mod

