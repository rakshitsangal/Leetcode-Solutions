class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            l=nums[:i]
            r=nums[i+1:]
            if sum(l)==sum(r):
                return i
        if i==len(nums)-1:
            return -1
