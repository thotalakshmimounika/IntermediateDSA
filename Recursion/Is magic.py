# Given a number A, check if it is a magic number or not.

# A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.



# Problem Constraints
# 1 <= A <= 109



# Input Format
# The first and only argument is an integer A.



# Output Format
# Return an 1 if the given number is magic else return 0.



# Example Input
# Input 1:

#  A = 83557
# Input 2:

#  A = 1291


# Example Output
# Output 1:

#  1
# Output 2:

#  0
import sys
sys.setrecursionlimit(10**6)
def recadd(a):
    if a==1:
        return 1
    if (a!=1 and a<=9):
        return 0
    ans=0
    while(a>0):
        ans+=a%10
        a=a//10

    return recadd(ans)

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, a):
        return recadd(a)

