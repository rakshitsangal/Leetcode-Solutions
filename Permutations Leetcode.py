class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def get_permute(part):
            if len(part) == len(nums):
                res.append(part.copy())
                return
            else:
                for x in nums:
                    if x not in part:
                        part.append(x)
                        get_permute(part)
                        part.pop()
                    
        get_permute([])
        return res
