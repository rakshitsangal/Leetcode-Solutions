class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		ans, lp, k = 0, 0, 1
		for rp in range(len(nums)):
			if nums[rp] == 0:
				k -= 1
			if k < 0:
				if nums[lp] == 0:
					k += 1
				lp += 1
			ans = max(ans, rp-lp)
		return ans
