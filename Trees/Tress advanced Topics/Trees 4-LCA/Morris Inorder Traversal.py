# Given a binary tree, return the inorder traversal of its nodes' values.

# NOTE: Using recursion and stack are not allowed.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is root node of the binary tree, A.



# Output Format
# Return an integer array denoting the inorder traversal of the given binary tree.



# Example Input
# Input 1:

#    1
#     \
#      2
#     /
#    3
# Input 2:

#    1
#   / \
#  6   2
#     /
#    3


# Example Output
# Output 1:

#  [1, 3, 2]
# Output 2:

#  [6, 1, 3, 2]


# Example Explanation
# Explanation 1:

#  The Inorder Traversal of the given tree is [1, 3, 2].
# Explanation 2:

#  The Inorder Traversal of the given tree is [6, 1, 3, 2].

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, a):
        ans=[]
        curr=a
        while(curr):
            if curr.left==None:
                ans.append(curr.val)
                curr=curr.right
            else:
                temp=curr.left
                while(temp.right!=None and temp.right!=curr):
                    temp=temp.right
                if temp.right==None:
                    temp.right=curr
                    curr=curr.left
                else:
                    temp.right=None
                    ans.append(curr.val)
                    curr=curr.right
        return ans

#Time complexity - O(3N)~O(N)
#Space complexity - O(1)