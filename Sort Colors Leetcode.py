class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = [num for color in [0, 1, 2] for num in nums if num == color]
