class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)<k:
            return s[::-1]
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)
	
