# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        flag = 0
        def dfs(root,pathSumSoFar):
            nonlocal flag
            if flag==0:
                if not root.left and not root.right:
                    pathSumSoFar+=root.val
                    if targetSum==pathSumSoFar:
                        flag = 1
                    return 
                if flag:
                    return
                if root.left:
                    dfs(root.left,pathSumSoFar+root.val)
                if root.right:
                    dfs(root.right,pathSumSoFar+root.val)
            return
        dfs(root,0)
        return flag==1
