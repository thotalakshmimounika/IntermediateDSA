# Given a binary tree,

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Assume perfect binary tree.



# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000

# 0 <= node values <= 10^9



# Input Format
# First and only argument is head of the binary tree A.



# Output Format
# Return the head of the binary tree after the changes are made.



# Example Input
# Input 1:

 
#      1
#     /  \
#    2    3
# Input 2:

 
#         1
#        /  \
#       2    5
#      / \  / \
#     3  4  6  7


# Example Output
# Output 1:

 
#         1 -> NULL
#        /  \
#       2 -> 3 -> NULL
# Output 2:

 
#          1 -> NULL
#        /  \
#       2 -> 5 -> NULL
#      / \  / \
#     3->4->6->7 -> NULL


# Example Explanation
# Explanation 1:

# Next pointers are set as given in the output.
# Explanation 2:

# Next pointers are set as given in the output.

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):

        dummy=TreeLinkNode(None)
        temp=dummy
        while(root):
            if root.left:
                temp.next=root.left
                temp=temp.next
            if root.right:
                temp.next=root.right
                temp=temp.next
            root=root.next
            if root==None:
                root=dummy.next
                dummy.next=None
                temp=dummy
        return root
#Time complexity - O(N)
#Spcae complexity - O(1)

#OR
# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        q=deque()
        q.append(root)
        while(q):
            s=len(q)
            while(s>1):
                root=q.popleft()
                root.next=q[0]
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                s-=1
            root=q.popleft()
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return root

#Time complexity - O(N)
#Spcae complexity - O(N)  



        
