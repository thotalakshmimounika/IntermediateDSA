# Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

# A-1 mod B is also known as modular multiplicative inverse of A under modulo B.



# Problem Constraints
# 1 <= A <= 109
# 1<= B <= 109
# B is a prime number



# Input Format
# First argument is an integer A.
# Second argument is an integer B.



# Output Format
# Return an integer denoting the modulor inverse



# Example Input
# Input 1:

#  A = 3
#  B = 5
# Input 2:

#  A = 6
#  B = 23


# Example Output
# Output 1:

#  2
# Output 2:

#  4


# Example Explanation
# Explanation 1:

#  Let's say A-1 mod B = X, then (A * X) % B = 1.
#  3 * 2 = 6, 6 % 5 = 1.
# Explanation 2:

#  Similarly, (6 * 4) % 23 = 1.

def POw(x,y,m):
    res=1
    x=x%m
    if x==0:
        return 0
    while(y>0):
        if ((y&1)==1):
            res=(res*x)%m
        y=y>>1
        x=(x*x)%m
    return res

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        ans=POw(a,b-2,b)
        return ans
#Time complexity - O(logn)- Logn base 2
#Space Complexity - O(1)