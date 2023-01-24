# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.



# Problem Constraints
# 1 <= N, M <= 105
# 1 <= A[i] <= 109
# 0 <= L <= R < N


# Input Format
# The first argument is the integer array A.
# The second argument is the 2D integer array B.


# Output Format
# Return an integer array of length M where ith element is the answer for ith query in B.


# Example Input
# Input 1:
# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
# Input 2:

# A = [2, 2, 2]
# B = [[0, 0], [1, 2]]


# Example Output
# Output 1:
# [10, 5]
# Output 2:

# [2, 4]


# Example Explanation
# Explanation 1:
# The sum of all elements of A[0 ... 3] = 1 + 2 + 3 + 4 = 10.
# The sum of all elements of A[1 ... 2] = 2 + 3 = 5.
# Explanation 2:

# The sum of all elements of A[0 ... 0] = 2 = 2.
# The sum of all elements of A[1 ... 2] = 2 + 2 = 4.


a = [ 7, 3, 1, 5, 5, 5, 1, 2, 4, 5 ]
b=[[6, 9],[2, 9],[2, 4],[0, 9]]
n=len(a)
p=[0]*(n+1)
print(n,p)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
print(p)
c=[]
for i in range(len(b)):
    l,r=b[i]
    c.append(p[r+1]-p[l])
print(c)