# Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).

# "^" means power,

# "%" means "mod", and

# "!" means factorial.



# Problem Constraints
# 1 <= A, B <= 5e5



# Input Format
# First argument is the integer A

# Second argument is the integer B



# Output Format
# Return one integer, the answer to the problem



# Example Input
# Input 1:

# A = 1
# B = 1
# Input 2:

# A = 2
# B = 2


# Example Output
# Output 1:

# 1
# Output 2:

# 4


# Example Explanation
# Explanation 1:

#  1! = 1. Hence 1^1 = 1.
# Explanation 2:

#  2! = 2. Hence 2^2 = 4.

def power(x, y, p) : 
    res = 1   
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1   
        x = (x * x) % p 
          
    return res

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def solve(self,a,b):
        m=10**9+7
        f=1
        for i in range(2,b+1):
            f=(f*i)%(m-1)
        return power(a,f,m)
#Time complexity - O(b+logb)
#Space complexity - O(1)
