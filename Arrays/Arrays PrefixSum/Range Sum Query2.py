#You are given an integer array A of length N.
#You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
#For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
#More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.


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