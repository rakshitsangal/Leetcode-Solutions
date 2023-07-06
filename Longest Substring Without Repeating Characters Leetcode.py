class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
        if len(l)==0:
            return 0
        a=len(l[0])
        for i in l:
            fl=0
            for j in i:
                if i.count(j)>1:
                    fl=1
                    break
            if fl==0:
                if len(i)>a:
                    a=len(i)
        return a
