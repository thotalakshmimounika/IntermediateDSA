#You are given an array A of N integers.Return a 2D array consisting of all the subarrays of the array
a = [1, 2, 3]
n=len(a)
s=[]
for i in range(n):
    for j in range(i,n):
        s.append(a[i:j])
print(s)