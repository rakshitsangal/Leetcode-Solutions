class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        a,b=0,1
        for i in s:
            if i not in ' -0123456789':
                break
            if i=='-':
                b=-1
            if '0'<=i<='9':
                a=a*10+int(i)
        return a*b
