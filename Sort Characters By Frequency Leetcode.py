from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=Counter(s)
        a=[]
        for key,value in sorted(l.items(), key = lambda x: -x[1]):
            a+=key*value
        return ''.join(a)
