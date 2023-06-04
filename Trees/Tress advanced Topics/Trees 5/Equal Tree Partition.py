# Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.



# Problem Constraints
# 1 <= size of tree <= 100000

# 0 <= value of node <= 109



# Input Format
# First and only argument is head of tree A.



# Output Format
# Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



# Example Input
# Input 1:

 
#                 5
#                /  \
#               3    7
#              / \  / \
#             4  6  5  6
# Input 2:

 
#                 1
#                / \
#               2   10
#                   / \
#                  20  2


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Remove edge between 5(root node) and 7: 
#         Tree 1 =                                               Tree 2 =
#                         5                                                     7
#                        /                                                     / \
#                       3                                                     5   6    
#                      / \
#                     4   6
#         Sum of Tree 1 = Sum of Tree 2 = 18
# Explanation 2:

#  The given Tree cannot be partitioned.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def treesum(self,root):
        if not root:
            return 0
        l=self.treesum(root.left)+self.treesum(root.right)+root.val
        self.sum_set.add(l)
        return l
    def solve(self, root):
        self.sum_set=set()
        s=self.treesum(root)
        if s//2 in self.sum_set:
            return 1
        return 0
#Time complexity - O(N)
#Spcae complexity - O(N)

#OR
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**6)
def treesum(root):
    if not root:
        return 0
    return treesum(root.left)+treesum(root.right)+root.val
class Solution:
    # @param A : root node of tree
    # @return an integer
    def func(self,root,s):
        if root==None:
            return 0
        l=self.func(root.left,s)
        r=self.func(root.right,s)
        if l==s//2 or r==s//2:
            self.ans=True
        return l+r+root.val

    def solve(self, root):
        s=treesum(root)
        if s%2==1:
            return 0
        else:
            self.ans=False
            self.func(root,s)
            if self.ans:
                return 1
            return 0

#Time complexity - O(2N)~O(N)
#Spcae complexity - O(H)