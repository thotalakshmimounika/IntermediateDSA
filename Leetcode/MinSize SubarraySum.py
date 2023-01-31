#leetcode prb no - 209
A=[2,3,1,4,3]
s = 7
i, res = 0, len(A) + 1
for j in range(len(A)):
    s -= A[j]
    while s <= 0:
        res = min(res, j - i + 1)
        s += A[i]
        i += 1
print(res % (len(A) + 1))

#Time complexity - O(n)
#space Complexity - O(1)