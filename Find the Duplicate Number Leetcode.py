class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for k in nums:
            a = abs(k)
            if nums[a-1] < 0: return a
            else:
                nums[a-1]*=-1
