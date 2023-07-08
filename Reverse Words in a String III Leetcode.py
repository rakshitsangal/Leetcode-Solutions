class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        l=[]
        for i in s:
            i=i[::-1]
            l.append(i)
        return ' '.join(l)
