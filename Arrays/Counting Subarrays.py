#Given an array A of N non-negative numbers and a non-negative number B,you need to find the number of subarrays in A with a sum less than B.We may assume that there is no overflow.
a= [2,5,6]
b = 10
n=len(a)
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=a[j]
        if s<b:
            c+=1
print(c)