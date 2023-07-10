class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C = {}
    	for i, n in enumerate(nums):
    		if n in C: C[n].append(i)
    		else: C[n] = [i]
    	M = max([len(i) for i in C.values()])
    	return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1
