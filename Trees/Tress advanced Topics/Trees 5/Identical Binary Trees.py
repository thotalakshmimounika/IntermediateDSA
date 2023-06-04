# Given two binary trees, check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# The first argument is a root node of the first tree, A.

# The second argument is a root node of the second tree, B.



# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



# Example Input
# Input 1:

#    1       1
#   / \     / \
#  2   3   2   3
# Input 2:

#    1       1
#   / \     / \
#  2   3   3   3


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Both trees are structurally identical and the nodes have the same value.
# Explanation 2:

#  Values of the left child of the root node of the trees are different.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, a,b):
        if a==None and b==None:
            return 1
        if a==None or b==None:
            return 0
        if a.val!=b.val:
            return 0
        return self.isSameTree(a.left,b.left) and self.isSameTree(a.right,b.right)
        


        

