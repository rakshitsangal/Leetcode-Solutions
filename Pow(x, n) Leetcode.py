class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        a=1
        for i in range(1,n+1):
            a*=x
        return a
