# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.


# Input Format

# The only argument given is the integer array A.
# Output Format

# Return the product array.
# Constraints

# 2 <= length of the array <= 1000
# 1 <= A[i] <= 10
# For Example

# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [120, 60, 40, 30, 24]

# Input 2:
#     A = [5, 1, 10, 1]
# Output 2:
#     [10, 50, 5, 50]

#If the product is too large take modulo 0f 10**9+7

a=[1,2,3,4]
n=len(a)
p=[1]*n
p[0]=a[0]
s=[1]*n
s[n-1]=a[n-1]
b=[]
m=10**9+7
for i in range(1,n):
    p[i]=(p[i-1]*a[i])%m
for i in range(n-2,-1,-1):
    s[i]=(s[i+1]*a[i])%m

for i in range(n):
    if i==0:
        b.append(s[i+1])
    elif i==n-1:
        b.append(p[i-1])
    else:
        b.append((p[i-1]*s[i+1])%m)
print(b)
    
	        
	        
