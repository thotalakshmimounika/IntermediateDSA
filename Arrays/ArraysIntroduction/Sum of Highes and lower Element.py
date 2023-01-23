#Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

a=[1,2,3,4,5]
h=a[0]
l=a[0]
for i in range(len(a)):
    if h<a[i]:
        h=a[i]
    if l>a[i]:
        l=a[i]
print(l+h)
