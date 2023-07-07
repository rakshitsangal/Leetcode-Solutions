class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vo=''.join(reversed([i for i in s if i in 'aeiouAEIOU']))
        a,b=0,''
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                b+=vo[a]
                a+=1
            else:
                b+=s[i]
        return b
