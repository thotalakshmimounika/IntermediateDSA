#You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.But the sum must not exceed B.
a = 5
b = 12
c = [2, 1, 3, 4, 5]

maxsum=0   
for i in range(a):
    s=0
    for j in range(i,a):
        s+=c[j]
        if s>=maxsum and s<=b:
            maxsum=s
print(maxsum)