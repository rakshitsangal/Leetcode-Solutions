class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum((n/a+8)/10*a + (n/a%10==1)*(n%a+1) for a in (10**pp for pp in range(10)))
