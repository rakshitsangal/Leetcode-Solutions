class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        l = s.split()
        if len(pattern) != len(l):
            return False
        hash = {}
        for key in range(len(pattern)):
            if pattern[key] not in hash and l[key] in hash.values():
                return False
            if pattern[key] not in hash:
                hash[pattern[key]] = l[key]
            elif hash[pattern[key]] != l[key]:
                return False
        return True
