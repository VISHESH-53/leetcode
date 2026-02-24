# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        return self.dfs(root,0)

    def dfs(self,node,curr):
        if not node:
            return 0
        curr =curr *2 +node.val
        if not node.left and not node.right:
            return curr
        return self.dfs(node.left,curr) + self.dfs(node.right, curr)
        
        
