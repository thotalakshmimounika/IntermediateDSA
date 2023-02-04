# Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.


# Problem Constraints
# 1 <= A <= 105


# Input Format
# The first argument is a single integer A.
# The second argument is an integer array B.


# Output Format
# Return the number of subarrays with bitwise array 1.


# Example Input
# Input 1:
#  A = 3
# B = [1, 0, 1]
# Input 2:
#  A = 2
# B = [1, 0]


# Example Output
# Output 1:
# 5
# Output2:
# 2


# Example Explanation
# Explanation 1:
# The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
# Except the subarray [0] all the other subarrays has a Bitwise OR = 1
# Explanation 2:
# The subarrays are :- [1], [0], [1, 0]
# Except the subarray [0] all the other subarrays has a Bitwise OR = 1
a=5
b=[ 0, 1, 0, 0, 0 ]
totalSubarrays= int((a*(a+1))/2)
print(totalSubarrays)
c=0
s=0
for i in b:
    if i==0:
        c+=1
    else:
        s+=int((c*(c+1))/2)
        c=0
if c>=1:
        s+=int((c*(c+1))/2)

print(totalSubarrays -s)
