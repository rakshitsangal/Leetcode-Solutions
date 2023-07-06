class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a,r = 0,len(numbers)-1
        while a<=r:
            if numbers[a]+numbers[r] == target:
                return [a+1,r+1]
            elif numbers[a]+numbers[r] > target:
                r -= 1
            else:
                a += 1
        return [a+1,r+1]
