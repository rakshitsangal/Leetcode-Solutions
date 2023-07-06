class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, sset):
            ans.append(sset[:])
            for k in range(start, len(nums)):
                sset.append(nums[k])
                backtrack(k + 1, sset)
                sset.pop()
                
        ans = []
        backtrack(0, [])
        return ans
