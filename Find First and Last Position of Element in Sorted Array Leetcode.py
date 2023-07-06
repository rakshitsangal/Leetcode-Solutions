class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                a=i
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                b=i
        return [b,a]
