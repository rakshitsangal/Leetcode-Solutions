class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        s=0
        while i<=j:
            if height[i]<height[j]:
                a=(j-i)*height[i]
                i+=1
            else:
                a=(j-i)*height[j]
                j-=1
            if s<a:
                s=a
        return s
