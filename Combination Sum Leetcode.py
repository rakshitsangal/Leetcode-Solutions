class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		ans = []
		def helps(x, path):
			if sum(path) == target:
				ans.append(path[:])
				return
			if sum(path) > target:
				return
			for i in range(x, len(candidates)):
				path.append(candidates[i])
				helps(i, path)
				path.pop()
		helps(0, [])
		return ans
