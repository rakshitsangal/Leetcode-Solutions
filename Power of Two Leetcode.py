class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        s,i=2,1
        while s<=n:
            s=pow(2,i)
            i+=1
            if s==n:
                return True
        return False
