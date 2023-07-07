# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1, n
        while True:
            m = a + (b-a) / 2
            if isBadVersion(m):
                b= m
            else:
                a= m + 1
            
            if b-a == 1:
                if isBadVersion(a):
                    return a
                return b
            elif a>=b:
                break
        return b
