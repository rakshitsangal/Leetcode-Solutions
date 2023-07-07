class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(0,n+1):
            s=str(bin(i))
            l.append(s.count('1'))
        return l
