class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote in magazine:
            return True
        chars = dict()
        for i in ransomNote:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 0
        for i in chars:
            if magazine.count(i) <= chars[i]: 
                return False
        return True
