# Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

# The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.

# Return the nodes in any order.



# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000

# 0 <= node values <= 10^9



# Input Format
# First and only argument is head of the binary tree A.



# Output Format
# Return an array, representing the top view of the binary tree.



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

#  [1, 2, 4, 8, 3, 7]
# Output 2:

#  [1, 2, 3]


# Example Explanation
# Explanation 1:

# Top view is described.
# Explanation 2:

# Top view is described.

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
        d={}
        q=deque()
        q.append((a,0))
        maxline,minline=0,0
        while(q):
            s=len(q)
            for i in range(s):
                curr=q.popleft()
                maxline=max(maxline,curr[1])
                minline=min(minline,curr[1])
                if curr[1] in d:
                    d[curr[1]].append(curr[0].val)
                else:
                    d[curr[1]]=[curr[0].val]
                if curr[0].left:
                    l=curr[1]-1
                    q.append((curr[0].left,l))
                if curr[0].right:
                    r=curr[1]+1
                    q.append((curr[0].right,r))
        ans=[]
        for i in range(minline,maxline+1):
            ans.append(d[i][0])
        return ans


            