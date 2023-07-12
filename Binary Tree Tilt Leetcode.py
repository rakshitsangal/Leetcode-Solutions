class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.total += abs(l - r)
            return l + r + node.val
        
        dfs(root)
        return self.total
