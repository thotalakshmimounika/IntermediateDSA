#You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
a = [ 20, 12, 15, 19, 13, 5, 13, 12, 18 ]
h=a[0]
ind=0
for i in range(1,len(a)):
    if h<a[i]:
        h=a[i]
        ind=i
s=-1
for i in range(len(a)):
    if s<a[i] and a[i]!=h:
        s=a[i]
print(s)