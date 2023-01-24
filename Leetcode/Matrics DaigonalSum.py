# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
a = [[7,9,8,6,3],[3,9,4,5,2],[8,1,10,4,10],[9,5,10,9,6],[7,2,4,10,8]]
n=len(a)
Sum=0

for i in range(n):
    Sum+=a[i][i]
    a[i][i]=0
    Sum+=a[i][n-1-i]
print(Sum)
