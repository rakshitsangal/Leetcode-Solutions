from functools import lru_cache
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        @lru_cache(None)
        def backtrack(i, j):
            if i == m and j == n:
                return True
            if i == m and j < n:
                if p[j] == "*" and backtrack(i, j + 1):
                    return True
            if i < m and j < n:
                if p[j] == "?" or s[i] == p[j]:
                    return backtrack(i + 1, j + 1)
                if p[j] == "*":
                    if (
                        backtrack(i + 1, j)
                        or backtrack(i, j + 1)
                        or backtrack(i + 1, j + 1)
                    ):
                        return True
            return False
        return backtrack(0, 0)
