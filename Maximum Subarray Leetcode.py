class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = float('-inf')
        maximum=0
        for num in nums:
            maximum += num
            sol = max(sol, maximum)
            maximum = max(maximum, 0)
        return sol
