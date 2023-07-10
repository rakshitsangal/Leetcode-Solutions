class Solution(object):
    def binary(self,nums,target,l,h):
        s=Solution()
        if l>h:
            return -1
        else:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return s.binary(nums,target,mid+1,h)
            else:
                return s.binary(nums,target,l,mid-1)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=Solution()
        a=s.binary(nums,target,0,len(nums)-1)
        return a
