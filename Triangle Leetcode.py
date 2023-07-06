class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        s=0
        for i in triangle:
            s+=min(i)
        return s
