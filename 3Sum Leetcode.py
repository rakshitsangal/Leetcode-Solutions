class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for iii in range(len(nums) - 2):
            a = nums[iii]
            if iii != 0 and a == nums[iii - 1]:
                continue
            l = iii + 1
            r = len(nums) - 1
            
            while l < r:
                b = nums[l]
                c = nums[r]
                threeSum = a + b + c
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, b, c])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
