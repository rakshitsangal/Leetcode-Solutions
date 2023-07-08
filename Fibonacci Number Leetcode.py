class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        a,b=0,1
        s=a+b
        for i in range(n-2):
            a=b
            b=s
            s=a+b
        return s
        
