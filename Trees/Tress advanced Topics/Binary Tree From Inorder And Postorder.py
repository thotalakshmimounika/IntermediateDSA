# Given the inorder and postorder traversal of a tree, construct the binary tree.

# NOTE: You may assume that duplicates do not exist in the tree.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First argument is an integer array A denoting the inorder traversal of the tree.

# Second argument is an integer array B denoting the postorder traversal of the tree.



# Output Format
# Return the root node of the binary tree.



# Example Input
# Input 1:

#  A = [2, 1, 3]
#  B = [2, 3, 1]
# Input 2:

#  A = [6, 1, 3, 2]
#  B = [6, 3, 2, 1]


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
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def ContructTree(self,a,b,sti,eni,stp,enp,d):
		if sti>eni: return
		root=b[enp]
		#find poistion on root.data in inorder
		ind=d[root]
		cntl=ind-sti
		x=TreeNode(root)
		x.left=self.ContructTree(a,b,sti,ind-1,stp,stp+cntl-1,d)
		x.right=self.ContructTree(a,b,ind+1,eni,stp+cntl,enp-1,d)
		return x
	def buildTree(self, a,b):
		n=len(a)
		sti,eni=0,n-1
		stp,enp=0,n-1
		d={}
		for i in range(n):
			d[a[i]]=i
		return self.ContructTree(a,b,sti,eni,stp,enp,d)

#Time complexity - O(N)
#Space Complexity - O(N)


