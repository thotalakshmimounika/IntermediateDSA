# Given preorder and inorder traversal of a tree, construct the binary tree.

# NOTE: You may assume that duplicates do not exist in the tree.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First argument is an integer array A denoting the preorder traversal of the tree.

# Second argument is an integer array B denoting the inorder traversal of the tree.



# Output Format
# Return the root node of the binary tree.



# Example Input
# Input 1:

#  A = [1, 2, 3]
#  B = [2, 1, 3]
# Input 2:

#  A = [1, 6, 2, 3]
#  B = [6, 1, 3, 2]


# Example Output
# Output 1:

#    1
#   / \
#  2   3
# Output 2:

#    1  
#   / \
#  6   2
#     /
#    3


# Example Explanation
# Explanation 1:

#  Create the binary tree and return the root node of the tree.

# Definition for a  binary tree node
class TreeNode:
  def init(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def constructTree(self, pre, ino, myHashmap, ps, pe, ins, ine) :
        if ins > ine :
            return None
        rootEle = pre[ps]
        rootIndex = myHashmap[rootEle]
        lenLst = rootIndex - ins
        x = TreeNode(rootEle)
        x.left = self.constructTree(pre, ino, myHashmap, ps + 1, ps + lenLst, ins, rootIndex - 1)
        x.right = self.constructTree(pre, ino, myHashmap, ps + lenLst + 1, pe, rootIndex + 1, ine)
        return x

    def buildTree(self, A, B):
        n = len(A)
        ps = 0
        pe = n - 1
        ins = 0
        ine = n - 1
        myHashmap = dict()
        for i in range(n) :
            myHashmap[B[i]] = i
        return self.constructTree(A, B, myHashmap, ps, pe, ins, ine)