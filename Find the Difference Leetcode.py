class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if s.count(i)==0:
                return i
            elif s.count(i)<t.count(i):
                return i
        
        
