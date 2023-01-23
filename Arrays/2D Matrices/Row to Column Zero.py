# You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.



# Problem Constraints
# 1 <= A.size() <= 103

# 1 <= A[i].size() <= 103

# 0 <= A[i][j] <= 103



# Input Format
# First argument is a vector of vector of integers.(2D matrix).



# Output Format
# Return a vector of vector after doing required operations.



# Example Input
# Input 1:

# [1,2,3,4]
# [5,6,7,0]
# [9,2,0,4]


# Example Output
# Output 1:

# [1,2,0,0]
# [0,0,0,0]
# [0,0,0,0]


# Example Explanation
# Explanation 1:

# A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.
a= [[1,2,3,4],[5,6,7,0],[9,2,0,4]]
rind=[]
cind=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==0:
            rind.append(i)
            cind.append(j)
            print(cind,rind)
print(cind,rind)
for i in rind:
    for j in range(len(a[0])):
        a[i][j]=0
print(a)
for i in cind:
    for j in range(len(a)):
        a[j][i]=0
print(a)