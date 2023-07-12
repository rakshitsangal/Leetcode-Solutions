class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=0
        for i in num:
            s=s*10+int(i)
        s+=k
        return [int(i) for i in str(s)]
