class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numA = 0
        for status in range(len(s)):
            if s[status] == 'A':
                numA += 1
            if s[status:status+3] == 'LLL':
                return False
        if numA >= 2:
            return False
        return True
