class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                temp = nums[i]
                break
        if k == -1:
            nums.sort()
            return

        l = -1
        for i in range(len(nums) - 1, k - 1, -1):
            if temp < nums[i]:
                l = i
                break
        
        nums[k] = nums[l]
        nums[l] = temp

        for i in range(k + 1, (k + 1 + len(nums)) // 2):
            t = nums[i]
            nums[i] = nums[len(nums) - 1 - (i - k - 1)]
            nums[len(nums) - 1 - (i - k - 1)] = t
   
        
