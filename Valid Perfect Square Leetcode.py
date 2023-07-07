class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=num**0.5
        if a==int(a):
            return True
        return False
