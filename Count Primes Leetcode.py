class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(2,n):
            fl=0
            for j in range(2,int(i**2)+1):
                if i%j==0:
                    fl=1
                    break
            if fl==0:
                c+=1
        return c
