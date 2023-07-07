class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=sum([int (i) for i in str(num)])
        if len(str(s))==1:
            return s
        while(len(str(s))!=1):
            s=sum([int(i) for i in str(s)])
        return s
