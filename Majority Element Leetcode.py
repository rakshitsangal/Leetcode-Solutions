class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        for i in l:
            if nums.count(i)>len(nums)//2:
                return i
