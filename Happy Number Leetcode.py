class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        while n>0:
            temp=0
            while n>0:
                temp+=(n%10)**2
                n//=10
            if temp in l:
                return False
            else:
                l.append(temp)
            if temp==1:
                return True
            n=temp
        return False
        
