class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        factors = [2, 3, 5]
        if n <= 0:
            return False
        for ii in factors:
            while n%ii == 0:
                n = n//ii
        return n == 1
