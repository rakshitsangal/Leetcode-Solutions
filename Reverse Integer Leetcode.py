class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 <=x<=2**31-1:
            s=0
            while x!=0:
                s+=x%10
                x=x//10
            return s
        else:
            return 0
        
