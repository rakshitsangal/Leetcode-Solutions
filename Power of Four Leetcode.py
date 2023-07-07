class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        s,i=4,1
        while s<=n:
            s=pow(4,i)
            i+=1
            if s==n:
                return True
        return False
