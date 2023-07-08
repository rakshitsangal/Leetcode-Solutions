class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        if len(l)<3:
            return max(l)
        l=sorted(l, reverse=True)
        return l[2]
