# Problem Description
# Given a decimal number A and base B.
# You are required to change the decimal number A into the corresponding value in base B and return that.

# Problem Constraints
# 0 <= A <= 512
# 2 <= B <= 10


# Input Format
# The first argument will be decimal number A.
# The second argument will be base B.


# Output Format
# Return the conversion of A in base B.


# Example Input
# Input:
# A = 4
# B = 3


# Example Output
# Output:
# 11


# Example Explanation
# Explanation:
# Decimal number 4 in base 3 is 11.

a= 4
b= 3
i=0
ans=0
while(a!=0):
    ans+=a%b*10**i
    a=a//b
    i+=1
print(ans)
