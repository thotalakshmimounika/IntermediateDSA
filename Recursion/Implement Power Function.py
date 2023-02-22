# Implement pow(A, B) % C.
# In other words, given A, B and C, Find (AB % C).

# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.



# Problem Constraints
# -109 <= A <= 109
# 0 <= B <= 109
# 1 <= C <= 109


# Input Format
# Given three integers A, B, C.


# Output Format
# Return an integer.


# Example Input
# A = 2, B = 3, C = 3


# Example Output
# 2


# Example Explanation
# 23 % 3 = 8 % 3 = 2

import sys
sys.setrecursionlimit(10**6)
def Pow(a,b,c):
    if a==0:
        return 0
    if b==0:
        return 1
    ans=Pow(a,b//2,c)
    if b%2==0:
        return ((ans%c)*(ans%c))%c
    if b%2==1:
        return ((ans%c)*(ans%c)*(a%c))%c


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        return Pow(A, B, C)

