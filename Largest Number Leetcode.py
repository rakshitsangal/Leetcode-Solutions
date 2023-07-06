class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = ''.join(sorted([str(a) for a in nums], 
                       key=lambda a: ((str(a)*9)[:9],a), 
                       reverse=True))
        return str(int(a))
