from sortedcontainers import SortedList
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        sn = SortedList(nums)
        for ii in nums:
            a = sn.index(ii)
            s.append(a)
            sn.remove(ii)
        return s
