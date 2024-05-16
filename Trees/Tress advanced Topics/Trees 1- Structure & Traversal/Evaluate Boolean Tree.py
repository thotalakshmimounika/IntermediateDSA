# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
n5=Node(1,None,None)
n4=Node(0,None,None)
n3=Node(3,n4,n5)
n2=Node(1,None,None)
root=Node(2,n2,n3)

class Solution:
    def evaluateTree(self, root:Node):
        def dfs(root):
            if root.val ==0 or root.val==1:
                return root.val
            elif root.val == 2:
                return dfs(root.left) or dfs(root.right)
            elif root.val == 3:
                return dfs(root.left) and dfs(root.right)
        return dfs(root)
obj=Solution()
result = obj.evaluateTree(root)
print(f"Final result of tree evaluation: {result}")