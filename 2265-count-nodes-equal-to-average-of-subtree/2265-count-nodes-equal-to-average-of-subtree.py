class Solution:
    def __init__(self):
        self.ctr=0
    def dfs(self,node):
        if node is None:
            return 0,0
        ls=self.dfs(node.left)
        rs=self.dfs(node.right)
        x=ls[0]+rs[0]+node.val
        n=ls[1]+rs[1]+1
        if x//n==node.val:
            self.ctr+=1
        return x,n
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.dfs(root)  
        return self.ctr
        