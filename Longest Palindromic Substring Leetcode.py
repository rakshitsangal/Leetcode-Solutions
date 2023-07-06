class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        b=''
        l=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
        for i in l:
            a=i[::-1]
            if a==i:
                if len(a)>len(b):
                    b=a
        return b
