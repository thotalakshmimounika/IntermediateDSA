# Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.


# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 109


# Input Format
# First and only argument is an array of integers A.


# Output Format
# Return the count of elements.


# Example Input
# Input 1:
# A = [3, 1, 2]
# Input 2:
# A = [5, 5, 3]


# Example Output
# Output 1:
# 2
# Output 2:
# 1


# Example Explanation
# Explanation 1:
# The elements that have at least 1 element greater than itself are 1 and 2
# Explanation 2:
# The elements that have at least 1 element greater than itself is 3

a=[1,4,6,2,7,9,3,9,3]
n = len(a)
max_el = a[0]
max_el_count = 0
for i in range(n):
    if a[i] >max_el:
        max_el = a[i]
        max_el_count = 1
    elif a[i]==max_el:
        max_el_count+=1
print(n - max_el_count)

# Time complexity - O(n)
#Space Complexity - O(1)
