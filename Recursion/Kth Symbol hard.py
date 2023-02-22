# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.).



# Problem Constraints
# 1 <= A <= 105

# 0 <= B <= min(2A - 1 - 1 , 1018)



# Input Format
# First argument is an integer A.

# Second argument is an integer B.



# Output Format
# Return an integer denoting the Bth indexed symbol in row A.



# Example Input
# Input 1:

#  A = 3
#  B = 0
# Input 2:

#  A = 4
#  B = 4


# Example Output
# Output 1:

#  0
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Row 1: 0
#  Row 2: 01
#  Row 3: 0110
# Explanation 2:

#  Row 1: 0
#  Row 2: 01
#  Row 3: 0110
#  Row 4: 01101001

def ans(A,B):
    if B==0 or B==1:
        return B

    x=ans(A-1,B//2)    # this will go to value and coordinate of parent elemnt

    if B%2==0:         # if the kid is at left index or even index, it will be same as parent elemnt
        return x
    else:              # otherwise if kid is at right or odd index, it will complimentray value
        return 1-x

class Solution:
    # @param A : integer
    # @param B : long
    # @return an integer
    def solve(self, A, B):
        return ans(A,B)    