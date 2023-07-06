class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup = 0
        for singleValue in range(1, len(nums)):
            if nums[ singleValue ] !=  nums[ lookup ]:
                lookup += 1
                nums[ lookup ] = nums[ singleValue ]
        return lookup + 1
