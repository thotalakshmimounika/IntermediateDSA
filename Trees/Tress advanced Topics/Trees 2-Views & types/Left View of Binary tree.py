# Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.

# Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

# NOTE: The value comes first in the array which have lower level.



# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000

# 0 <= node values <= 109



# Input Format
# First and only argument is a root node of the binary tree, A.



# Output Format
# Return an integer array denoting the left view of the Binary tree.



# Example Input
# Input 1:

#             1
#           /   \
#          2    3
#         / \  / \
#        4   5 6  7
#       /
#      8 
# Input 2:

#             1
#            /  \
#           2    3
#            \
#             4
#              \
#               5


# Example Output
# Output 1:

#  [1, 2, 4, 8]
# Output 2:

#  [1, 2, 4, 5]

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, a):
        ans=[]
        q=deque()
        q.append(a)
        while(q):
            s=len(q)
            for i in range(1,s+1):
                x=q.popleft()
                if i==1:
                    ans.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return ans

