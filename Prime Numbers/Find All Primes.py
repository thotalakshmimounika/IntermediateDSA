# Given an integer A. Find the list of all prime numbers in the range [1, A].


# Problem Constraints
# 1 <= A <= 106



# Input Format
# Only argument A is an integer.



# Output Format
# Return a sorted array of prime number in the range [1, A].



# Example Input
# Input 1:
# A = 7
# Input 2:
# A = 12


# Example Output
# Output 1:
# [2, 3, 5, 7]
# Output 2:
# [2, 3, 5, 7, 11]


# Example Explanation
# For Input 1:
# The prime numbers from 1 to 7 are 2, 3, 5 and 7.
# For Input 2:
# The prime numbers from 1 to 12 are 2, 3, 5, 7 and 11.
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, a):
        p=[0]*(a+1)
        ans=[]
        for i in range(2,len(p)):
            if p[i]==0:
                for j in range(2*i,len(p),i):
                    p[j]=1
        for i in range(2,len(p)):
            if p[i]==0:
                ans.append(i)
        return ans

#Method Used - Sieve of Eratosthenes
#Time Complexity - O(nlog(logn))
#space Complexity - O(n) -- for array p