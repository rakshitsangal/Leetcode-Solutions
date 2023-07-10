class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        count=0
        left,right=0,1
        length=len(nums)
        while left<length:
            product=1
            right=left
            while right<length:
                product*=nums[right]
                if product<k:
                    right+=1
                else:
                    break
            count+=(right-left)
            left+=1
            if right==length:
                count+=int((right-left+1)*(right-left)/2)
                break
        return count
