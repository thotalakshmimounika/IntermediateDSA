# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# NOTE:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.
a=[1,3,4,2,2]

n=len(a)
ls=0
rs=sum(a)
for i in range(n):
    if i==0:
        rs-=a[i]
    else:
        rs-=a[i]
        ls+=a[i-1]
    if ls==rs:
        print(i)
        break
else:
    print(-1)

# Time complexity - O(N)
#Space Complexity - O(1)

#or

#Using Prefix sum
for i in range(1,n):
    a[i]=a[i]+a[i-1]
    
for i in range(n):
    if i==0:
        val = 0
    else:
        val = a[i-1]

    if val == a[n-1] - a[i]:
        return i

return -1

# Time complexity - O(N)
#Space Complexity - O(N)
