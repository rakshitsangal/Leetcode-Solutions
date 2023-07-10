class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            a=s[0]
            s=s[1::]
            s+=a
            if s==goal:
                return True
        return False
