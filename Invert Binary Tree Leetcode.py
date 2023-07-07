class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        def invert(root):
            if root:
                interval = root.left
                root.left = root.right
                root.right = interval
                invert(root.left)
                invert(root.right)
            return 0
        invert(root)
        return node
    
