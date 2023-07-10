class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0 : k])
        ma= s
        for i in range(0, len(nums) - k):
            s = s + nums[i + k] - nums[i]
            ma = max(ma, s)
        return ma/ k
