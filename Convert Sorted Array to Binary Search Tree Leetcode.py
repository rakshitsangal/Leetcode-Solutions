# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums,l,r):
            if l>r:
                return None
            mid=(l+r)//2
            newNode=TreeNode(nums[mid])
            newNode.left=helper(nums,l,mid-1)
            newNode.right=helper(nums,mid+1,r)
            return newNode
			
        if len(nums)==0:
            return None
        else:
            return helper(nums,0,len(nums)-1)
