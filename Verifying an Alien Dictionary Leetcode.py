class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        l = []
        for kk in words:
            l.append([order.index(a) for a in kk])
        return l == sorted(l)
