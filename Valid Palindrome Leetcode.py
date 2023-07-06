class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a,b='',''
        for i in s:
            if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
                if 'A'<=i<='Z':
                    i=i.lower()
                a+=i
        if a=='':
            return True
        for i in range(len(a)-1,-1,-1):
            b+=a[i]
        print(b)
        if a==b:
            return True
        else:
            return False
