# Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

# NOTE:

# Rows are numbered from top to bottom, and columns are numbered from left to right.
# Sum may be large, so return the answer mod 109 + 7.


# Problem Constraints
# 1 <= N, M <= 1000
# -100000 <= A[i] <= 100000
# 1 <= Q <= 100000
# 1 <= B[i] <= D[i] <= N
# 1 <= C[i] <= E[i] <= M



# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer array B.
# The third argument given is the integer array C.
# The fourth argument given is the integer array D.
# The fifth argument given is the integer array E.
# (B[i], C[i]) represents the top left corner of the i'th query.
# (D[i], E[i]) represents the bottom right corner of the i'th query.



# Output Format
# Return an integer array containing the submatrix sum for each query.



# Example Input
# Input 1:

#  A = [   [1, 2, 3]
#          [4, 5, 6]
#          [7, 8, 9]   ]
#  B = [1, 2]
#  C = [1, 2]
#  D = [2, 3]
#  E = [2, 3]
# Input 2:

#  A = [   [5, 17, 100, 11]
#          [0, 0,  2,   8]    ]
#  B = [1, 1]
#  C = [1, 4]
#  D = [2, 2]
#  E = [2, 4]


# Example Output
# Output 1:

#  [12, 28]
# Output 2:

#  [22, 19]


# Example Explanation
# Explanation 1:

#  For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
#  For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
# Explanation 2:

#  For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
#  For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, a,b,c,d,e):
        n=len(a)
        m=len(a[0])
        for i in range(n):
            for j in range(1,m):
                a[i][j]=a[i][j-1]+a[i][j]
        for i in range(m):
            for j in range(1,n):
                a[j][i]=a[j-1][i]+a[j][i]
        ans=[]
        for i in range(len(b)):
            x1=b[i]-1
            y1=c[i]-1
            x2=d[i]-1
            y2=e[i]-1
            m=a[x2][y2]
            if y1>0:
                m-=a[x2][y1-1]
            if x1>0:
                m-=a[x1-1][y2]
            if x1>0 and y1>0:
                m+=a[x1-1][y1-1]
            ans.append(m%(10**9 + 7))
        return ans

#Time Complexity - O(N*M + Q)
#Space Complexity - O(N*M)
            
