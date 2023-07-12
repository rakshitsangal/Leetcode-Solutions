# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def heightAndpath(root):
            if not root:
                return [0, 0]
            ld, lp = heightAndpath(root.left)
            rd, rp = heightAndpath(root.right)
            return [1 + max(ld, rd), max(lp, rp, ld + rd)]
        return heightAndpath(root)[1]
