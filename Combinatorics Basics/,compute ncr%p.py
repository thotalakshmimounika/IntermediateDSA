# Given three integers A, B, and C, where A represents n, B represents r, and C represents p and p is a prime number greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.

# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.

# NOTE: For this problem, we are considering 1 as a prime.



# Problem Constraints
# 1 <= A <= 106
# 1 <= B <= A
# A <= C <= 109+7


# Input Format
# The first argument given is the integer A ( = n).
# The second argument given is the integer B ( = r).
# The third argument given is the integer C ( = p).



# Output Format
# Return the value of nCr % p.



# Example Input
# Input 1:

#  A = 5
#  B = 2
#  C = 13
# Input 2:

#  A = 6
#  B = 2
#  C = 13


# Example Output
# Output 1:

#  10
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  nCr( n=5 and r=2) = 10.
#  p=13. Therefore, nCr%p = 10.


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
    # @param C : integer
    # @return an integer
    def solve(self, a,b,c):
        if c==1:
            return 0
        v1=max(a,b)
        v2=min(b,a-b)
        n=1
        d=1
        for i in range(v2):
            n=(n*(v1-i))%c
            d=(d*(i+1))%c
        finalde= pow(d,c-2,c)
        return ((n%c)*(finalde%c))%c

#Time complexity - O(max(a,b,c))
#space complexity - O(1)- used fast power function - binary method
