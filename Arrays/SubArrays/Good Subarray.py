#Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
#1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
#2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.Your task is to find the count of good subarrays in A.
a = [1, 2, 3, 4, 5]
b = 4  
n=len(a)
c=0
for i in range(n):
    s=0
    l=0
    for j in range(i,n):
        s+=a[j]
        if s<b and len(a[i:j+1])%2==0 or s>b and len(a[i:j+1])%2==1:
            c+=1
print(c)



