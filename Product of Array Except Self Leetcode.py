class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * (l := len(nums)), [1]*l
        for i in range(1, l):
            left[i] *= left[i-1]*nums[i-1]
            right[-i-1] *= right[-i]*nums[-i]
        return [lv*rv for lv, rv in zip(left, right)]
