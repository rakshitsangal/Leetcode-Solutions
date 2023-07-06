class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        l=s.split(' ')
        a=l[len(l)-1]
        return len(a)
