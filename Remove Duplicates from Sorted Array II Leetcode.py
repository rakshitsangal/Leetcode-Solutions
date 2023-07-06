class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        s=set(nums)
        for i in s:
            if nums.count(i)>2:
                c+=2
                for j in range(len(nums)-1,-1,-1):
                    if nums[j]==i:
                        if nums.count(i)>2:
                            nums.remove(i)
            else:
                c+=nums.count(i)
        return c
       
