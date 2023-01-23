# Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.


# Problem Constraints
# 1<= N <= 1000
# 1<= A[i][j] <= 1e9


# Input Format
# Only argument is a 2D array A of size N * N.


# Output Format
# Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
# The vacant spaces in the grid should be assigned to 0.


# Example Input
# Input 1:
# 1 2 3
# 4 5 6
# 7 8 9
# Input 2:

# 1 2
# 3 4


# Example Output
# Output 1:
# 1 0 0
# 2 4 0
# 3 5 7
# 6 8 0
# 9 0 0
# Output 2:

# 1 0
# 2 3
# 4 0


# Example Explanation
# For input 1:
# The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
# The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
# The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
# The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
# The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
# For input 2:

# The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
# The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
# The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        n=len(a)
        ans=[[0]*len(a) for _ in range(2*len(a)-1)]
        r=-1
        c=-1
        for i in range(n):
            s_r=0
            s_c=i
            r+=1
            c=0
            while(s_r<n and s_c>=0):
                ans[r][c]=a[s_r][s_c]
                s_r+=1
                s_c-=1
                c+=1
        r=n-1
        c=0
        for i in range(1,n):
            s_r=i
            s_c=n-1
            r+=1
            c=0
            while(s_r<n and s_c>=0):
                ans[r][c]=a[s_r][s_c]
                s_r+=1
                s_c-=1
                c+=1
        return ans


#Time Complexity - O(N*N)
#Space Complexity - O(N*N)
