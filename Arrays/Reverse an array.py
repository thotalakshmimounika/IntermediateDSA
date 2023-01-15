#You are given a constant array A.
#You are required to return another array which is the reversed form of the input array.
a=[ 1, 2, 3, 2, 1 ]
s=[]
n=len(a)
for i in range(len(a)):
    s.append(a[n-i-1])
print(s)