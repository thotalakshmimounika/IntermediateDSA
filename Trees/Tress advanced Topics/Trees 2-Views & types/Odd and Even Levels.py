# Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.

# NOTE: Consider the level of root node as 1.



# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000

# 0 <= node values <= 109



# Input Format
# First and only argument is a root node of the binary tree, A



# Output Format
# Return an integer denoting the difference between the sum of nodes at odd level and sum of nodes at even level.



# Example Input
# Input 1:

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#   /
#  8 
# Input 2:

#         1
#        / \
#       2   10
#        \
#         4


# Example Output
# Output 1:

#  10
# Output 2:

#  -7


# Example Explanation
# Explanation 1:

#  Sum of nodes at odd level = 23
#  Sum of ndoes at even level = 13
# Explanation 2:

#  Sum of nodes at odd level = 5
#  Sum of ndoes at even level = 12

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, a):
        q=deque()
        odd_s=0
        even_s=0
        q.append(a)
        i=1
        while(q):
            s=len(q)
            if i%2==1:
                for j in range(s):
                    x=q.popleft()
                    odd_s+=(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
            else:
                for j in range(s):
                    x=q.popleft()
                    even_s+=(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
            i+=1
        return odd_s-(even_s)

