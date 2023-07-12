class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=max((max(A) - min(A) - 2*K), 0)
        return a
