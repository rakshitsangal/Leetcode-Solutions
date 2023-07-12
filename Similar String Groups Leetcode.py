class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, x):
        if self.parents[x] != x:
            return self.find(self.parents[x])
        return x
    
    def union(self, u, v):
        self.parents[self.find(u)] = self.find(v)

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:     
        def isSimilar(s, t):
            swaps = 0
            l, r = 0, len(s) - 1
            while l <= r:
                if (s[l] != t[l] and s[r] != t[r]):
                    if s[l] != t[r] or s[r] != t[l]: return False
                    l += 1
                    r -= 1
                    swaps += 1
                if s[l] == t[l]: l += 1
                if s[r] == t[r]: r -= 1
            return swaps <= 1

        seen = UnionFindSet(len(strs))
        for i in range(len(strs)):
            for j in range(len(strs)):
                if isSimilar(strs[i], strs[j]):
                    seen.union(i, j)

        parents = set()
        for i in range(len(strs)):
            parent = seen.find(i)
            if parent not in parents:
                parents.add(parent)

        return len(set(parents))
