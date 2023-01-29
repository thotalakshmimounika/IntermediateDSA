# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



# Problem Constraints
# 1 <= n <= 105
# -105 <= A[i] <= 105


# Input Format
# First argument contains an array A of integers of size N


# Output Format
# Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



# Example Input
# Input 1:
# A=[2, 1, 6, 4]
# Input 2:

# A=[1, 1, 1]


# Example Output
# Output 1:
# 1
# Output 2:

# 3


# Example Explanation
# Explanation 1:
# Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
# Therefore, the required output is 1. 
# Explanation 2:

# Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
# Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
# Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
# Therefore, the required output is 3.

a=[2, 1, 6, 4]
n=len(a)
pfe=[0]*n
pfo=[0]*n
pfe[0]=a[0]
for i in range(n):
    if i%2==1:
        pfe[i]=pfe[i-1]
    else:
        pfe[i]=a[i]+pfe[i-1]
print(pfe)
for i in range(n):
    if i%2==0:
        pfo[i]=pfo[i-1]
    else:
        pfo[i]=pfo[i-1]+a[i]
print(pfo)
c=0
for i in range(n):
    if i==0:
        if pfe[n-1]-pfe[0]==pfo[n-1]-pfo[0]:
            c+=1
    else:
        es=0
        es=pfe[i-1]+(pfo[n-1]-pfo[i])
        os=0
        os=pfo[i-1]+(pfe[n-1]-pfe[i])
        if es==os:
            c+=1
print(c)