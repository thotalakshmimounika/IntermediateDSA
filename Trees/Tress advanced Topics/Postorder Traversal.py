# Given a binary tree, return the Postorder traversal of its nodes values.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is root node of the binary tree, A.



# Output Format
# Return an integer array denoting the Postorder traversal of the given binary tree.



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

#  [3, 2, 1]
# Output 2:

#  [6, 3, 2, 1]


# Example Explanation
# Explanation 1:

#  The Preoder Traversal of the given tree is [3, 2, 1].
# Explanation 2:

#  The Preoder Traversal of the given tree is [6, 3, 2, 1].

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, a):
        ans=[]
        stack=[]
        while(a or stack):
            if a!=None:
                stack.append(a)
                a=a.left
            else:
                temp=stack[-1].right
                if temp==None:
                    temp=stack.pop()
                    ans.append(temp.val)
                    while(stack and temp==stack[-1].right):
                        temp=stack.pop()
                        ans.append(temp.val)               
                else:
                    a=temp
        return ans
#Time complexity - O(2N)
#Space complexity - O(height of stack)