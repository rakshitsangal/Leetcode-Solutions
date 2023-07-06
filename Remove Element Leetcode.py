class Solution:
    def removeElement(self, nums, val):
        a = 0
        for x in nums:
            if x != val:
                nums[a] = x
                a += 1
        return a
