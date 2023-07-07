class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        le = len(nums)
        su = (le * (le + 1)) // 2
        li_sum = sum(nums)
        return su - li_sum
