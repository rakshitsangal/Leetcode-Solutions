# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root, isLeft):
            if(root == None):
                return 0 
            if(root.left == None and root.right ==None and isLeft):
                return root.val
            return traverse(root.left,True) + traverse(root.right,False)
        return traverse(root,False)
