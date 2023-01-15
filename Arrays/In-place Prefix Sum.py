#Given an array A of N integers. Construct prefix sum of the array in the given array itself.

a = [1, 2, 3, 4, 5]
for i in range(1,len(a)):
    a[i]=a[i]+a[i-1]
print(a)