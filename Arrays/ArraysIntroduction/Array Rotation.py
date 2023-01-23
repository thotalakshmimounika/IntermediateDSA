# Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.


# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <=109
# 1 <= B <= 109


# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.


# Output Format
# Return the array A after rotating it B times to the right


# Example Input
# Input 1:

# A = [1, 2, 3, 4]
# B = 2
# Input 2:

# A = [2, 5, 6]
# B = 1


# Example Output
# Output 1:

# [3, 4, 1, 2]
# Output 2:

# [6, 2, 5]


# Example Explanation
# Explanation 1:

# Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]
# Explanation 2:

# Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]

a= [ 1, 1, 4, 9, 4, 7, 1 ]
b= 9

a=a[::-1]
print(a[:b][::-1]+(a[b:][::-1]))

#Reverse the Whole array then split the array into two parts - start to b , b to end. Then swap the elements internally

# time complexity - to reverse - O(n) + swap the elements - O(n)
# Space complexity - O(1)
