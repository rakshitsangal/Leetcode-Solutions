class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums.sort()
        mid = (length-1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
