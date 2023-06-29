# You are given an array A of N integers and three integers B, C, and D.

# You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



# Problem Constraints

# 1 <= N <= 105

# -10000 <= A[i], B, C, D <= 10000



# Input Format

# First argument is an array A
# Second argument is an integer B
# Third argument is an integer C
# Fourth argument is an integer D



# Output Format

# Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



# Example Input

# Input 1:

#  A = [1, 5, -3, 4, -2]
#  B = 2
#  C = 1
#  D = -1
# Input 2:

#  A = [3, 2, 1]
#  B = 1
#  C = -10
#  D = 3


# Example Output

# Output 1:

#  18
# Output 2:

#  -4

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self,a,b,c,d):
        n=len(a)
        pf_max1=[0]*n
        pf_max2=[0]*n
        pf_max3=[0]*n

        pf_max1[0]=a[0]*b
        pf_max2[0]=pf_max1[0]+a[0]*c
        pf_max3[0]=pf_max2[0]+a[0]*d

        for i in range(1,n):
            pf_max1[i]=max(pf_max1[i-1],a[i]*b)
            pf_max2[i]=max(pf_max2[i-1],pf_max1[i]+a[i]*c)
            pf_max3[i]=max(pf_max3[i-1],pf_max2[i]+a[i]*d)
        return max(pf_max3)

#TC - O(N)
#SC - O(N)