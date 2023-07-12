# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
        # If there are no more subtrees from root to compare we return false
        if not r:
            return False
        # Recursive check to see if any subtree in root is the same as the sub root tree
        if self.is_same(r, sr):
            return True
        # If there exists a subtree in the left or right branch of root that matches -
        # the sub root tree we return true
        return self.isSubtree(r.left, sr) or self.isSubtree(r.right, sr)

    
    # Function returns true if two trees are the same structurally with identical values
    def is_same(self, r,sr) -> bool:
        if not r and not sr:
            return True
        if r and sr and r.val == sr.val:
            return (self.is_same(r.left, sr.left) 
                    and self.is_same(r.right, sr.right))
        return False
                 
                 
