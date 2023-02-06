# You are given a large number in the form of a array A of size N where each element denotes a digit of the number.
# You are also given a number B. You have to find out the value of A % B and return it.



# Problem Constraints
# 1 <= N <= 105
# 0 <= Ai <= 9
# 1 <= B <= 109


# Input Format
# The first argument is an integer array A.
# The second argument is an integer B.


# Output Format
# Return a single integer denoting the value of A % B.


# Example Input
# Input 1:
# A = [1, 4, 3]
# B = 2
# Input 2:

# A = [4, 3, 5, 3, 5, 3, 2, 1]
# B = 47

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        p=1
        ans=0
        for i in range(n-1,-1,-1):
            ans= (ans%b+(a[i]%b * (p)%b))%b
            p= (p%b * 10%b)%b
        return ans