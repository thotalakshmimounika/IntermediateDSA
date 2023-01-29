# There are A people standing in a circle. Person 1 kills their immediate clockwise neighbour and pass the knife to the next person standing in circle. This process continues till there is only 1 person remaining. Find the last person standing in the circle.


# Problem Constraints
# 1 <= A <= 105


# Input Format
# First argument A is an integer.


# Output Format
# Return an integer.


# Example Input
# Input 1:
# A = 4
# Input 2:
# A = 5


# Example Output
# Output 1:
# 1
# Output 2:
# 3


# Example Explanation
# For Input 1:
# Firstly, the person at position 2 is killed, then the person at position 4 is killed,
# then the person at position 3 is killed. So the person at position 1 survives. 
# For Input 2:
 
# Firstly, the person at position 2 is killed, then the person at position 4 is killed, 
# then the person at position 1 is killed. Finally, the person at position 5 is killed. 
# So the person at position 3 survives. 



# See Expected Output

class Solution:
    import math
    # @param A : integer
    # @return an integer
    def solve(self, a):
        kills_req= (2**(math.floor(math.log2(a))))
        return 2*(a-kills_req)+1

# by making the remaining people exactly pow of 2 after some skills, the next person , who is holding the sword will win.
#here we are checking the closest pow of 2 to given number and calsulating how many skill required.
#for killing 'x' people we need 'x' other person . So in total '2x' people will involve in this kill and next person who holds the sword will survive.
