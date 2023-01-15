#You are given an integer array A of length N.
#You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
#For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
#More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]
n = len(A)
prefix_sum = [0] * (n+1)
print(prefix_sum)
for i in range(1,len(A)+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    print(prefix_sum)
print(prefix_sum)
print(len(B),B[0])
result = []
for i in range(len(B)):
    l, r = B[i]
    result.append(prefix_sum[r] - prefix_sum[l-1])
print(result)
