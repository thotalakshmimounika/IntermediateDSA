# Given an integer A.

# Compute and return the square root of A.

# If A is not a perfect square, return floor(sqrt(A)).

# DO NOT USE SQRT FUNCTION FROM THE STANDARD LIBRARY.

# NOTE: Do not use the sqrt function from the standard library. Users are expected to solve this in O(log(A)) time.



# Problem Constraints
# 0 <= A <= 1010



# Input Format
# The first and only argument given is the integer A.



# Output Format
# Return floor(sqrt(A))



# Example Input
# Input 1:

#  11
# Input 2:

#  9


# Example Output
# Output 1:

#  3
# Output 2:

#  3


# Example Explanation
# Explanation:

#  When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
#  When A = 9 which is a perfect square of 3, so we return 3.

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, a):
        n=a
        left=1
        right=n-1
        if a==0 or a==1:
            return a
        while (left<=right):
            mid=(left+right)//2
            val=mid*mid
            if val==a:
                ans=mid
                break
            elif val>a:
                right=mid-1
            else:
                ans=mid
                left=mid+1
        return ans

#Time complexity - O(log(1-a))
# Space Complexity - O(1)   
            



