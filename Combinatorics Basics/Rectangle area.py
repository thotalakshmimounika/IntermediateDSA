# Given eight integers A, B, C, D, E, F, G, and H, which represent two rectangles in a 2D plane.

# For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

# Find and return the overlapping area of the two rectangles.



# Problem Constraints
# -104 <= A <= C <= 104
# -104 <= B <= D <= 104
# -104 <= E <= G <= 104
# -104 <= F <= H <= 104


# Input Format
# The eight arguments given are the integers A, B, C, D, E, F, G and H.



# Output Format
# Return the overlapping area of the two rectangles.



# Example Input
# Input 1:

#  A = 0   B = 0
#  C = 4   D = 4
#  E = 2   F = 2
#  G = 6   H = 6
# Input 2:

#  A = 0   B = 0
#  C = 4   D = 4
#  E = 2   F = 2
#  G = 3   H = 3


# Example Output
# Output 1:

#  4
# Output 2:

#  1


# Example Explanation

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, a,b,c,d,e,f,g,h):
        if(g<=a or e>=c or h<=b or f>=d):
            return 0
        x1=max(a,e)
        x2=min(c,g)
        y1=max(b,f)
        y2=min(d,h)
        return abs((x2-x1)*(y2-y1))
