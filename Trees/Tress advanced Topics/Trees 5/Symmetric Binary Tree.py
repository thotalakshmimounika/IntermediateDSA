# Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is the root node of the binary tree.



# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ).



# Example Input
# Input 1:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# Input 2:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  The above binary tree is symmetric. 
# Explanation 2:

# The above binary tree is not symmetric.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, a,b):
        if a==None and b==None:
            return 1
        if a==None or b==None:
            return 0
        if a.val!=b.val:
            return 0
        return self.isSameTree(a.left,b.right) and self.isSameTree(a.right,b.left)
    def isSymmetric(self, root):
        return self.isSameTree(root,root)
    

