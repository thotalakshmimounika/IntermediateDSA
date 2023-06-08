# Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is root node of the binary tree, A.



# Output Format
# Return a 2D integer array denoting the level order traversal of the given binary tree.



# Example Input
# Input 1:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Input 2:

#    1
#   / \
#  6   2
#     /
#    3


# Example Output
# Output 1:

#  [
#    [3],
#    [9, 20],
#    [15, 7]
#  ]
# Output 2:

#  [ 
#    [1]
#    [6, 2]
#    [3]
#  ]


# Example Explanation
# Explanation 1:

#  Return the 2D array. Each row denotes the traversal of each level.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, a):
        if a==None:
            return []
        root=a
        q=deque()
        q.append(root)
        ans=[]
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                currnode=q.popleft()
                if currnode:
                    q.append(currnode.left)
                    q.append(currnode.right)

                    level.append(currnode.val)
            if level:
                ans.append(level)
        return ans
        
        

